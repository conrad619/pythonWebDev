import requests
from flask import Flask, session, redirect, url_for, escape, request

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

app = Flask(__name__)
app.secret_key = b'\xe5\xbf\xfcP\xa6$nM~\xf3~\xd0\x18\xc6\x1e\x11'
@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
