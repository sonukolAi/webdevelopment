import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)
PORT = 3330

@app.route('/<num>')
def get_train_status(num):
    #      https://trainstatus.com/runningstatus/{num}  .panel-heading
    #      https://spotyourtrain.com/trainstatus?train={num} .table-success  
    url = f"https://runningstatus.in/status/{num}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        train_name = soup.find('head').text.replace('Live Train Running Status', '').strip()
        current_station = soup.find(class_='table-success').text.strip()
        
        data = {
            'Name': train_name,
            'currentStation': current_station
        }
        return data
    else:
        return 'Error retrieving data', 500

if __name__ == '__main__':
    app.run(port=PORT)
