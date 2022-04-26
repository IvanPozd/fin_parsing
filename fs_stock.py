import csv
import time

from bs4 import BeautifulSoup
from datetime import date
from get_html_selenium import generate_html
from selenium.common.exceptions import NoSuchElementException


def main_fs_stock():
    url = "https://www.finscreener.org/screener/fs-stock-ranking?o=2&pg="

    with open(f"./output/fs_stock_{date.today()}.csv", "w", encoding="utf-8", newline="") as file:
        fields = [
            "Date",
            "Rank",
            "Ticker",
            "Finscreen Rank",
            "Change 3M",
            "3M",
            "6M",
            "12M",
            "Value Rank",
            "Grows Rank",
            "Income Rank",
            "Analyst Rank",
            "History",
            "Empty",
        ]
        writer = csv.DictWriter(file, fields, delimiter=",")
        writer.writeheader()

    for page_number in range(1, 6):
        time.sleep(3)
        all_data = [get_data(generate_html(f"{url}{page_number}"))]
        add_to_csv(all_data)
        print(f"Added data from - {url}{page_number}")

    print("Wrote CSV file!")


def add_to_csv(array):
    with open(f"./output/fs_stock_{date.today()}.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for page_data in array:
            for block in page_data:
                writer.writerow(block)
    

def get_data(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="table")
        trs = table.find_all("tr")
        number = 0
        one_page_data = []

        for tr in trs:
            tds = tr.find_all("td")
            number += 1
            if len(tds) != 0:
                if number > 2:
                    company_data = []
                    today = date.today()
                    company_data.append(today)
                    for i in tds:
                        company_data.append(i.text)
                    one_page_data.append(company_data)

        return one_page_data

    except NoSuchElementException:
        print("No such element!")
