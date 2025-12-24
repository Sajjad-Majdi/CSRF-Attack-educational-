# CSRF Proof of Concept: Plan & Architecture

## 1. Project Overview

This project demonstrates a Cross-Site Request Forgery (CSRF) attack for educational purposes. It consists of two separate entities:

- **Victim Site (SecureCrypto):** A vulnerable cryptocurrency exchange dashboard.
- **Attacker Site (YouWonPrize):** A malicious phishing page that triggers a hidden request to the victim site.

## 2. Technical Architecture

### Victim Site: SecureCrypto

- **Backend:** Python (Flask)
- **Database:** SQLite (In-memory or local file) for user sessions and data.
- **Authentication:** Cookie-based session management (`flask.session`).
- **Vulnerability:** The `/change-email` endpoint lacks CSRF protection (no tokens, no SameSite=Strict enforcement).
- **Design Theme:** _The Obsidian Vault_ (Luxury/Refined, Dark Mode, Glassmorphism).

### Attacker Site: YouWonPrize

- **Frontend:** Static HTML/JS.
- **Payload:** A hidden HTML form that auto-submits to `http://localhost:5000/change-email`.
- **Design Theme:** _Dopamine Overload_ (Maximalist Chaos, Neon, High Urgency).

## 3. Implementation Details

### Directory Structure

```
CSRF Attack/
├── victim_app/
│   ├── app.py              # Flask application logic
│   └── templates/
│       ├── login.html      # Secure-looking login
│       └── dashboard.html  # Vulnerable dashboard
├── attacker_app/
│   └── exploit.html        # The malicious payload
└── README.md               # Setup and execution guide
```

### Security Flaw Explanation

The victim site relies solely on the browser's automatic inclusion of cookies for authentication. When a logged-in user visits the attacker's site, the attacker's script triggers a POST request to the victim's server. The browser attaches the victim's session cookie to this request, and the server processes it as a legitimate action from the user.

## 4. Design Vision (Frontend Design Skill)

### SecureCrypto (Victim)

- **Typography:** Cinzel (Headings) & IBM Plex Mono (Data).
- **Colors:** `#0a0a0a` (Background), `#00ff9d` (Emerald Accent).
- **Effects:** Glassmorphism panels, subtle grid backgrounds, slow transitions.

### YouWonPrize (Attacker)

- **Typography:** Bangers (Headings) & Comic Neue (Body).
- **Colors:** Electric Purple, Bright Yellow, Neon Red.
- **Effects:** Confetti, pulsing buttons, scrolling marquees, chaotic layout.
