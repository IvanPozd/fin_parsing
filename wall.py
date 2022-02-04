import csv
import time

from bs4 import BeautifulSoup
from datetime import date
from get_html_selenium import generate_html
from selenium.common.exceptions import NoSuchElementException


def main_wall():
    for page in range(1, 30):
        time.sleep(1)
        all_data = [
            get_data(
                generate_html(
                    f"https://www.wallstreetzen.com/stock-screener?p={page}&s=t&sd=asc&t=2"
                )
            )
        ]
        add_to_csv(all_data)
        print(
            f"Added data from https://www.wallstreetzen.com/stock-screener?p={page}&s=t&sd=asc&t=2"
        )


def additional_wall():
    for page in range(30, 63):
        time.sleep(1)
        all_data = [
            get_data(
                generate_html(
                    f"https://www.wallstreetzen.com/stock-screener?p={page}&s=t&sd=asc&t=2"
                )
            )
        ]
        add_to_csv(all_data)
        print(
            f"Added data from https://www.wallstreetzen.com/stock-screener?p={page}&s=t&sd=asc&t=2"
        )

    print("Wrote a CSV file")


def add_to_csv(array):
    with open(f"wall_street_stock_{date.today()}.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for page in array:
            for block in page:
                writer.writerow(block)


def get_data(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("tbody")
        trs = body.find_all("tr")
        one_page_data = []
        for tr in trs:
            tds = tr.find_all("td")
            company_data = []
            today = date.today()
            company_data.append(today)
            for td in tds:
                company_data.append(td.text)
            one_page_data.append(company_data)

        return one_page_data

    except NoSuchElementException:
        print("No such element!Error")
