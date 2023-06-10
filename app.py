from selenium import webdriver

@app.route('/<num>')
def get_train_status(num):
    try:
        url = f"https://www.google.com/search?q={num}+train+running+status"

        # Use Selenium to perform the request
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        response = driver.page_source

        modified_html = modify_html(response)  # Modify the HTML response
        driver.quit()  # Quit the browser

        return modified_html
    except Exception as e:
        return f"Error: {str(e)}"
