
# DOKUMENTACJA PROJEKTU

## PhishGuard – Edukacyjny Symulator Phishingu

**Autorzy:** Michał Kostrzewa, Jakub Jędrzejewski, Jan Cielesz  

---

## 1. Wstęp

### 1.1 Cel projektu

Celem projektu **PhishGuard** jest podniesienie świadomości użytkowników w zakresie cyberbezpieczeństwa poprzez symulację ataku phishingowego. Aplikacja imituje stronę logowania popularnego serwisu społecznościowego (Facebook), a po wprowadzeniu danych – zamiast kradzieży – prezentuje interaktywny raport edukacyjny.

### 1.2 Zakres funkcjonalny

System składa się z dwóch głównych modułów:

- **Symulator ataku (Frontend):** Wierna kopia strony logowania z mechanizmem przechwytywania danych w celach edukacyjnych.
- **Panel edukacyjny (Raport):**
  - Analiza siły hasła
  - Sprawdzenie wycieków danych (integracja z Have I Been Pwned)
  - Prezentacja cyfrowego śladu (Digital Footprint)
  - Quiz edukacyjny z rozpoznawania fałszywych domen

---

## 2. Architektura Systemu

### 2.1 Stos technologiczny

- **Frontend:**
  - HTML5
  - React 18 (ładowany przez CDN)
  - Tailwind CSS (stylizacja)
  - Babel (transpilacja JSX w locie)
  - SPA (Single Page Application)
- **Backend:**
  - Python 3.x
  - Flask
- **Komunikacja:** REST API (JSON)
- **Zewnętrzne API:**
  - Have I Been Pwned (HIBP)
  - Pwned Passwords
  - ipapi.co (geolokalizacja)
  - OpenStreetMap

### 2.2 Diagram przepływu danych

1. Użytkownik wchodzi na stronę `index.html`.
2. Wprowadza dane logowania na fałszywym formularzu.
3. Frontend przechwytuje dane i przełącza widok na panel edukacyjny.
4. Frontend wysyła zapytania do lokalnego backendu (`server.py`) w celu weryfikacji wycieków emaila i hasła.
5. Backend komunikuje się z serwisami zewnętrznymi (HIBP), omijając zabezpieczenia anty-botowe (Cloudflare) przy użyciu Selenium.
6. Wyniki są prezentowane użytkownikowi wraz z ostrzeżeniami.

---

## 3. Instalacja i Konfiguracja

### 3.1 Wymagania wstępne

- Python 3.9 lub nowszy
- Przeglądarka Google Chrome
- Dostęp do Internetu

### 3.2 Instalacja zależności (Backend)

W katalogu projektu zainstaluj wymagane biblioteki Python:

```bash
pip install flask flask-cors undetected-chromedriver selenium requests
