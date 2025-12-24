from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'super-secret-key-for-educational-purposes'

# Database setup
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)')
        # Add a default user if not exists
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', ('alice',))
        if not cursor.fetchone():
            conn.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                         ('alice', 'password123', 'alice@securecrypto.com'))
        conn.commit()


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT id, username, email FROM users WHERE username = ? AND password = ?', (username, password))
            user = cursor.fetchone()

            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                session['email'] = user[2]
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials', 'error')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Fetch latest email from DB
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT email FROM users WHERE id = ?',
                       (session['user_id'],))
        email = cursor.fetchone()[0]
        session['email'] = email

    return render_template('dashboard.html', username=session['username'], email=session['email'])


@app.route('/change-email', methods=['POST'])
def change_email():
    if 'user_id' not in session:
        return "Unauthorized", 401

    new_email = request.form.get('email')
    if new_email:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('UPDATE users SET email = ? WHERE id = ?',
                         (new_email, session['user_id']))
            conn.commit()
        flash(f'Email successfully updated to {new_email}', 'success')

    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    init_db()
    # Default away from port 5000 on Windows (some environments block it).
    host = os.getenv('SECURECRYPTO_HOST', '127.0.0.1')
    try:
        port = int(os.getenv('SECURECRYPTO_PORT', '5050'))
    except ValueError:
        port = 5050

    # Disable the reloader to avoid double-bind issues in some setups.
    app.run(debug=True, host=host, port=port, use_reloader=False)
