import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template_string

app = Flask(__name__)
PORT = 3330

@app.route('/<num>')
def get_train_status(num):
    try:
        url = f"https://www.google.com/search?q={num}+train+running+status"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        data = response.text
        modified_data = modify_html(data)
        return render_template_string(modified_data)
    except Exception as e:
        print(e)
        return 'Error occurred', 500

def modify_html(data):
    soup = BeautifulSoup(data, 'html.parser')
    train_name = soup.select('div.k9rLYb')[0].text.strip()
    live_status = soup.select('div.dK1Bub .rUtx7d')[1].text
    delay_time = soup.select('div.Rjvkvf.MB86Dc')[1].text.strip()

    modified_html = f'''
    <html>
    <head>
        <title>Train Status</title>
    </head>
    <body>
        <h1>Train Status</h1>
        <p>Train Name: {train_name}</p>
        <p>Live Status: {live_status}</p>
        <p>Delay Time: {delay_time}</p>
    </body>
    </html>
    '''

    return modified_html

if __name__ == '__main__':
    app.run(port=PORT)
