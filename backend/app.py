from flask import Flask, jsonify, Response
from flask_cors import CORS
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import json
import time
import requests

app = Flask(__name__)
CORS(app)


@app.route('/check/<email>', methods=['GET'])
def check_breach(email):
    print(f"[*] Rozpoczynam sprawdzanie dla: {email} przy użyciu Chrome...")
    options = uc.ChromeOptions()

    driver = None
    try:
        driver = uc.Chrome(options=options, use_subprocess=True)

        driver.get("https://google.com")
        time.sleep(1)

        url = f"https://haveibeenpwned.com/unifiedsearch/{email}"

        driver.get(url)

        time.sleep(4)

        body_text = driver.find_element(By.TAG_NAME, "body").text

        print(f"[*] Pobrana treść: {body_text[:100]}...")  # Logowanie początku odpowiedzi

        try:
            data = json.loads(body_text)
            return jsonify(data)
        except json.JSONDecodeError:
            return jsonify(
                {"error": "Otrzymano HTML zamiast JSON. Prawdopodobnie blokada Cloudflare.", "raw": body_text}), 503

    except Exception as e:
        print(f"[!] Błąd Selenium: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        # Bardzo ważne: zamykamy przeglądarkę po zakończeniu żądania
        if driver:
            driver.quit()


@app.route('/range/<prefix>', methods=['GET'])
def check_password_range(prefix):
    if len(prefix) != 5:
        return jsonify({"error": "Prefix must be 5 chars"}), 400

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url)
        return Response(response.text, mimetype='text/plain')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)