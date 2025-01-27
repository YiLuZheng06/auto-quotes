import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def fetch_quote():
    url = "https://go-quote.azurewebsites.net/random-quote"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
    except Exception as e:
        print(f"Error fetching quote: {e}")
    return {"text": "Unable to fetch quote", "author": "Unknown"}


@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    email = data.get('email', 'No email provided')
    pwd = data.get('pwd', 'No password provided')

    try:

        quote = fetch_quote()

        HOST = "smtp.zoho.com"
        PORT = 587
        FROM_EMAIL = email
        TO_EMAIL = "YOUR_RECIPIENT@gmail.com"
        PASSWORD = pwd

        message = MIMEMultipart("alternative")
        message['Subject'] = "Mail sent using python"
        message['From'] = FROM_EMAIL
        message['To'] = TO_EMAIL
        message['Cc'] = FROM_EMAIL
        message['Bcc'] = FROM_EMAIL

        html = f"""
            <h1>Hello! 👋</h1>
            <h3>Your quote today is:</h3>
            <p>{quote['text']}</p>
            <p>-{quote['author']}</p>
        """

        html_port = MIMEText(html, 'html')
        message.attach(html_port)

        with smtplib.SMTP(HOST, PORT) as smtp:
            status_code, response = smtp.ehlo()
            print(f"[*] Echoing the server: {status_code} {response}")

            status_code, response = smtp.starttls()
            print(f"[*] Starting TLS connection: {status_code} {response}")

            status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
            print(f"[*] Logging in: {status_code} {response}")

            # sends the email
            smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
            smtp.quit()

        return jsonify({'success': True, 'message': 'Authentication successful.'})
    except Exception as e:
        print(f"SMTP Error: {e}")
        return jsonify({'success': False, 'message': 'Authentication failed.'})


@app.route('/getQuotes', methods=['GET'])
def getQuotes():
    # gets a random quote
    quote = fetch_quote()
    return jsonify(quote)


@app.route('/dailyQuotes', methods=['GET'])
def dailyQuotes():
    # Fetch a new quote for display on the daily quotes page
    quote = fetch_quote()
    return render_template('dailyQuotes.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)