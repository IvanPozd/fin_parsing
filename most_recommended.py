import csv
import time

from bs4 import BeautifulSoup
from datetime import date
from get_html_selenium import generate_html
from selenium.common.exceptions import NoSuchElementException


def main_most_recommended():
    url = "https://www.finscreener.org/analysts/most-recommended-stocks?o=8&pg="
    
    for page_number in range(1, 6):
        time.sleep(3)
        all_data = [get_data(generate_html(f"{url}{page_number}"))]
        add_to_csv(all_data)
        print(f"Added data from - {url}{page_number}")

    print("wrote CSV file!")


def add_to_csv(array):
    with open(f"most_recomended_{date.today()}.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for page_data in array:
            if len(page_data) > 20:
                writer.writerows(page_data)


def get_data(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="table")
        trs = table.find_all("tr")
        data = []
        for tr in trs:
            tds = tr.find_all("td")
            company = []
            today = date.today()
            company.append(today)
            for td in tds:
                company.append(td.text.replace("\n", " "))
            if len(company) > 1:
                data.append(company)
        return data

    except NoSuchElementException:
        print("No Such Element")
