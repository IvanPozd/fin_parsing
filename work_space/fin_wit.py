import os
import requests
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def generate_html(url, retry=5):
    try:
        proxy = {"https": "https://194.124.49.23:8000"}
        options = Options()
        options.headless = False
        service = Service(executable_path=ChromeDriverManager().install())
        base_dir = os.path.join(os.path.dirname(__file__))
        browser_chrome = webdriver.Chrome(
            executable_path=f'{base_dir}/chromedriver',
            options=options,
            service=service
            )
        browser_chrome.get(url)
        WebDriverWait(browser_chrome, 5)
        page_email = browser_chrome.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[1]/div/div/input')
        page_email.clear()
        page_email.send_keys('guillaume.graf@yahoo.com')

        page_pass = browser_chrome.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/input')
        page_pass.clear()
        page_pass.send_keys('GGraf1436!')

        #rec_but = browser_chrome.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
        #rec_but.click()

        button = browser_chrome.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[4]/button')
        button.click()
        
        #generated_html = browser.page_source
        #browser.quit()
                

    except requests.exceptions.ConnectionError:
        print("Check Your Internet Connection")
        time.sleep(3)
        if retry:
            print(f"[INFO] retry={retry} => {url}")
            return generate_html(url, retry=(retry - 1))
        else:
            raise


def main():
    URL = 'https://fintwit.ai/sign-in'
    generate_html(URL)


if __name__ == '__main__':
    main()