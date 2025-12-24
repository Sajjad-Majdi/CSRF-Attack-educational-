from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('exploit.html')


if __name__ == '__main__':
    host = os.getenv('ATTACKER_HOST', '127.0.0.1')
    try:
        port = int(os.getenv('ATTACKER_PORT', '8080'))
    except ValueError:
        port = 8080

    print(f"\n🎯 Attacker site running at http://{host}:{port}")
    print(f"📌 Make sure the victim site is running and you're logged in before visiting!\n")

    app.run(debug=True, host=host, port=port, use_reloader=False)
