# CSRF Proof of Concept (Educational)

This project demonstrates a Cross-Site Request Forgery (CSRF) attack.

## Prerequisites

- Python 3.x
- Flask (`pip install flask`)

## Setup Instructions

### 1. Start the Victim Site (SecureCrypto)

1. Open a terminal in the `victim_app` directory.
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. The site will be available at `http://127.0.0.1:5050`.

### 2. Start the Attacker Site (YouWonPrize)

1. Open a **second terminal** in the `attacker_app` directory.
2. Run the attacker's Flask server:
   ```bash
   python app.py
   ```
3. The attacker site will be available at `http://127.0.0.1:8080`.

### 3. Log in to the Victim Site

1. Open your browser and go to `http://127.0.0.1:5050/login`.
2. Use the following credentials:
   - **Username:** `alice`
   - **Password:** `password123`
3. You will be redirected to the dashboard, showing your current email: `alice@securecrypto.com`.

### 4. Execute the Attack

1. **IMPORTANT:** Keep the Victim Site tab open and logged in (simulating an active session).
2. Open a **NEW TAB** in the same browser and visit `http://127.0.0.1:8080`.
3. You will see a flashy "You Won an iPhone!" page.
4. After 1 second, the page will silently send a malicious request in the background to the Victim Site.
5. The exploit page will **stay visible** (you won't be redirected).

### 5. Verify the Result

1. Go back to the SecureCrypto dashboard tab (or refresh it).
2. Look at the "Current Email" - it will have changed to `hacker@evil.com`.
3. The attack succeeded without you noticing!

## How it Works

The Victim Site (`SecureCrypto`) does not use CSRF tokens. It relies solely on the session cookie for authentication. When you visit the Attacker Site while logged into SecureCrypto, the browser automatically includes your session cookie in the request triggered by the attacker's hidden form. The server sees a valid cookie and processes the email change request as if you had performed it yourself.

## Prevention

To fix this vulnerability, the Victim Site should:

1. Implement **CSRF Tokens**: A unique, secret, and unpredictable token for each session.
2. Use **SameSite Cookie Attribute**: Set cookies to `SameSite=Lax` or `SameSite=Strict`.
3. Verify the **Origin/Referer** headers.
