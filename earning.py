import csv
import time

from bs4 import BeautifulSoup
from datetime import date
from get_html_selenium import generate_html
from selenium.common.exceptions import NoSuchElementException


def main_earning():
    url = "https://www.finscreener.org/earnings/earnings-estimates?o=1013&pg="
    
    with open(f"earning_est_{date.today()}.csv", "w", encoding="utf-8", newline="") as file:
        fields = [
            "Date",
            "Ticker",
            "Period End",
            "Current",
            "7 D ago",
            "30 D ago",
            "60 D ago",
            "90 D ago",
            "EPS Est. Revision % ",
            "Trend",
        ]
        writer = csv.DictWriter(file, fields, delimiter=",")
        writer.writeheader()

    for page in range(1, 6):
        time.sleep(3)
        all_data = [(get_data(generate_html(f"{url}{page}")))]
        add_to_csv(all_data)
        print(f"Added data from - {url}{page}")

    print("Wrote a CSV file")


def add_to_csv(array):
    with open(f"earning_est_{date.today()}.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for page_data in array:
            for company in page_data:
                writer.writerow(company)


def get_data(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="table")
        trs = table.find_all("tr")
        one_page_data = []
        for tr in trs:
            tds = tr.find_all("td")
            if len(tds) != 0:
                company_data = []
                today = date.today()
                company_data.append(today)
                for td in tds:
                    company_data.append(td.text)
                one_page_data.append(company_data)
        return one_page_data

    except NoSuchElementException:
        print("No such element!Error")
