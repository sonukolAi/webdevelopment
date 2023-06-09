import requests
from bs4 import BeautifulSoup
from flask import Flask

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
        modified_data = modify_json(data)
        return modified_data
    except Exception as e:
        print(e)
        return 'Error occurred', 500

def modify_json(data):
    soup = BeautifulSoup(data, 'html.parser')
    train_name = soup.select('div.k9rLYb')[0].text.strip()
    live_status = soup.select('div.dK1Bub .rUtx7d')[1].text
    delay_time = soup.select('div.Rjvkvf.MB86Dc')[1].text.strip()

    return {
        'trainName': train_name,
        'liveStatus': live_status,
        'delayTime': delay_time
    }

if __name__ == '__main__':
    app.run(port=PORT)
