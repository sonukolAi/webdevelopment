import requests
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
        modified_html = modify_html(response.text)  # Modify the HTML response
        return modified_html
    except Exception as e:
        return f"Error: {str(e)}"

def modify_html(html):
    # Implement your logic to modify the HTML response here
    # You can use libraries like BeautifulSoup to parse and manipulate the HTML
    modified_html = html  # Placeholder, modify the HTML as per your requirements
    return modified_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
