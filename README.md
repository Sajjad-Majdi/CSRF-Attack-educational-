# CSRF Proof of Concept (Educational)

This project demonstrates a Cross-Site Request Forgery (CSRF) attack.

## Prerequisites

- Python 3.x
- Flask (`pip install flask`)

## Setup Instructions

### 1. Start the Victim Site (SecureCrypto)

1. Navigate to the `victim_app` directory.
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. The site will be available at `http://localhost:5000`.

### 2. Log in to the Victim Site

1. Open your browser and go to `http://localhost:5000/login`.
2. Use the following credentials:
   - **Username:** `alice`
   - **Password:** `password123`
3. You will be redirected to the dashboard, showing your current email: `alice@securecrypto.com`.

### 3. Execute the Attack

1. Keep the Victim Site tab open (simulating an active session).
2. Open a new tab and open the `attacker_app/exploit.html` file directly in your browser (or serve it via another local server).
3. The page will load with a "You Won" message and immediately trigger a hidden request to the Victim Site.
4. You will be redirected back to the Victim Site's dashboard.

### 4. Verify the Result

1. Look at the "Current Email" on the SecureCrypto dashboard.
2. It should now be changed to `hacker@evil.com`.

## How it Works

The Victim Site (`SecureCrypto`) does not use CSRF tokens. It relies solely on the session cookie for authentication. When you visit the Attacker Site while logged into SecureCrypto, the browser automatically includes your session cookie in the request triggered by the attacker's hidden form. The server sees a valid cookie and processes the email change request as if you had performed it yourself.

## Prevention

To fix this vulnerability, the Victim Site should:

1. Implement **CSRF Tokens**: A unique, secret, and unpredictable token for each session.
2. Use **SameSite Cookie Attribute**: Set cookies to `SameSite=Lax` or `SameSite=Strict`.
3. Verify the **Origin/Referer** headers.
