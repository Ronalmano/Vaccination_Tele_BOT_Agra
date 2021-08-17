# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from datetime import datetime
from telegram.ext import *

base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
api_url_telegram = "https://api.telegram.org/bot1801002278:AAF5R0tnm2EvvAyZT6EAU6vnrGz-pKkSPHs/sendMessage?chat_id=@demo_agra_cowin&text="
group_id = "demo_agra_cowin"
agra_district_id = [141, 142, 143, 144, 145, 146, 147, 148, 149, 150]


def fetch_data(district_id):
    query_param = "?district_id={}&date={}".format(district_id, today_date)
    final_url = base_url+query_param
    response = requests.get(final_url)
    extract_data(response)
    # print(response.text)


def extract_data(response):
    response_json = response.json()
    for center in response_json["centers"]:
        for sessions in center["sessions"]:
            if sessions["available_capacity_dose1"] > 0:
                message = "Pincode: {}, \nName: {}, \nSlots: {}, \nMinimum Age: {}, \nAddress: {}, \nRegistration link ={}".format(
                    center["pincode"], center["name"], sessions["available_capacity_dose1"], sessions["min_age_limit"],
                    center["address"], "https://selfregistration.cowin.gov.in/")
                send_message_tele(message)


def send_message_tele(message):
    final_telegram_url = api_url_telegram
    final_telegram_url = final_telegram_url + message
    response = requests.get(final_telegram_url)
    print(response)


if __name__ == "__main__":
    fetch_data(622)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
