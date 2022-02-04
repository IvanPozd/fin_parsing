import os
import requests
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager


def generate_html(url, retry=5):
    try:
        proxy = {"https": "https://194.124.49.23:8000"}
        options = Options()
        options.headless = True
        service = Service(executable_path=GeckoDriverManager().install())
        base_dir = os.path.join(os.path.dirname(__file__))
        browser = webdriver.Firefox(
            executable_path=f"{base_dir}/geckodriver", options=options, service=service, proxy=proxy
        )
        browser.get(url)
        generated_html = browser.page_source
        browser.quit()
        return generated_html

    except requests.exceptions.ConnectionError:
        print("Check Your Internet Connection")
        time.sleep(3)
        if retry:
            print(f"[INFO] retry={retry} => {url}")
            return generate_html(url, retry=(retry - 1))
        else:
            raise

    except TimeoutException:
        print("WebSite is not available")
        time.sleep(3)
        if retry:
            print(f"[INFO] retry={retry} => {url}")
            return generate_html(url, retry=(retry - 1))
        else:
            raise
