# Importing some modules and setting up a few properties
import sys
import os
from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
sys.path.append(os.getcwd())
os.environ["DJANGO_SETTINGS_MODULE"] = "tsdb_app.settings"

import django
django.setup()
from core import backup




def main():
    backup.main()
    fund_source_location()
    fund_source_funding_possibility()
    organization_location()
    organization_category()
    organization_status()
    social_post_platform()
    product_price()
    consumer_location()
    consumer_age()


def height_calc(num):
    if num <= 2:
        return 2
    
    elif num <= 5:
        return 4

    elif num <= 10:
        return 7
    
    elif num <= 20:
        return 10

    else:
        return 15


def fund_source_location():
    with open("backupfiles/FundSourceBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        location_dict = Counter()

        next(my_reader)
        for line in my_reader:
            location_dict.update([line[1]])  

        temp_tuple_list = sorted(dict(location_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("FUND SOURCES' LOCATION")
        plt.xlabel("Number Of Fund Sources")
        plt.ylabel("Location")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot1.png")


def fund_source_funding_possibility():
    with open("backupfiles/FundSourceBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        possibility_dict = Counter()

        next(my_reader)
        for line in my_reader:
            possibility_dict.update([line[4]])  

        temp_tuple_list = sorted(dict(possibility_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])

        colors = ["#0e8f13", "#0AB210", "#0ffc17"]
        plt.style.use("seaborn")
        plt.figure(figsize=(10,4))
        _, _, autotexts = plt.pie(y_value, labels=x_value , colors=colors, wedgeprops={"edgecolor":"white"}, autopct="%1.1f%%")
        for autotext in autotexts:
            autotext.set_color('white')

        plt.title("FUND SOURCES' FUNDING POSSIBILITY")
        plt.tight_layout()
        plt.savefig("static/images/plots/plot2.png")


def organization_location():
    with open("backupfiles/OrganizationBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        location_dict = Counter()

        next(my_reader)
        for line in my_reader:
            location_dict.update([line[1]])   

        temp_tuple_list = sorted(dict(location_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("ORGANIZATIONS' LOCATION")
        plt.xlabel("Number Of Organizations")
        plt.ylabel("Location")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot3.png")


def organization_category():
    with open("backupfiles/OrganizationBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        category_dict = Counter()

        next(my_reader)
        for line in my_reader:
            category_dict.update([line[2]])  

        temp_tuple_list = sorted(dict(category_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])

        colors = ["#0e8f13", "#0AB210", "#0ffc17", "#9dff7d"]
        plt.style.use("seaborn")
        plt.figure(figsize=(10,4))
        _, _, autotexts = plt.pie(y_value, labels=x_value , colors=colors, wedgeprops={"edgecolor":"white"}, autopct="%1.1f%%")
        for autotext in autotexts:
            autotext.set_color('white')

        plt.title("ORGANIZATIONS' CATEGORY")
        plt.tight_layout()
        plt.savefig("static/images/plots/plot4.png")


def organization_status():
    with open("backupfiles/OrganizationBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        status_dict = Counter()

        next(my_reader)
        for line in my_reader:
            status_dict.update([line[5]])  

        temp_tuple_list = sorted(dict(status_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])

        colors = ["#0e8f13", "#0AB210"]
        plt.style.use("seaborn")
        plt.figure(figsize=(10,4))
        _, _, autotexts = plt.pie(y_value, labels=x_value , colors=colors, wedgeprops={"edgecolor":"white"}, autopct="%1.1f%%")
        for autotext in autotexts:
            autotext.set_color('white')

        plt.title("ORGANIZATIONS' STATUS")
        plt.tight_layout()
        plt.savefig("static/images/plots/plot5.png")


def social_post_platform():
    with open("backupfiles/SocialPostBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        platform_dict = Counter()

        next(my_reader)
        for line in my_reader:
            platform_dict.update([line[0]])  

        temp_tuple_list = sorted(dict(platform_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])

        colors = ["#191a18", "#0e8f13", "#0AB210", "#0ffc17", "#9dff7d"]
        plt.style.use("seaborn")
        plt.figure(figsize=(10,4))
        _, _, autotexts = plt.pie(y_value, labels=x_value , colors=colors, wedgeprops={"edgecolor":"white"}, autopct="%1.1f%%")
        for autotext in autotexts:
            autotext.set_color('white')

        plt.title("SOCIALPOSTS' PLATFORM")
        plt.tight_layout()
        plt.savefig("static/images/plots/plot6.png")


def product_price():
    with open("backupfiles/ProductBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        price_list = []

        next(my_reader)
        for line in my_reader:
            price = int(line[1])
            price_list.append(price)  

        lowest = min(price_list)
        highest = max(price_list)
        bins = [0]

        current = lowest
        while current <= highest:
            bins.append(current)
            current += 500
        bins.append(current)

        plt.style.use("seaborn")
        plt.figure(figsize=(10, 6))
        plt.hist(price_list, bins=bins, color="#0AB210", edgecolor="#ffffff")

        plt.title("PRODUCTS' PRICE")
        plt.xlabel("Price")
        plt.ylabel("Number of Products")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot7.png")


def consumer_location():
    with open("backupfiles/ConsumerBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        location_dict = Counter()

        next(my_reader)
        for line in my_reader:
            location_dict.update([line[3]])   

        temp_tuple_list = sorted(dict(location_dict).items(), key=lambda x:x[1])
        x_value = []
        y_value = []
        for tup in temp_tuple_list:
            x_value.append(tup[0])
            y_value.append(tup[1])
        height_num = len(x_value)

        plt.style.use("seaborn")
        plt.figure(figsize=(10,height_calc(height_num)))
        plt.barh(x_value, y_value , color="#0AB210")

        plt.title("CONSUMERS' LOCATION")
        plt.xlabel("Number Of Consumers")
        plt.ylabel("Location")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot8.png")


def consumer_age():
    with open("backupfiles/ConsumerBUF.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        age_list = []

        next(my_reader)
        for line in my_reader:
            age = int(line[2])
            age_list.append(age)  

        lowest = min(age_list)
        highest = max(age_list)
        bins = [0]

        current = lowest
        while current <= highest:
            bins.append(current)
            current += 5
        bins.append(current)

        plt.style.use("seaborn")
        plt.figure(figsize=(10, 6))
        plt.hist(age_list, bins=bins, color="#0AB210", edgecolor="#ffffff")

        plt.title("CONSUMERS' AGE")
        plt.xlabel("Age")
        plt.ylabel("Number of Consumers")

        plt.tight_layout()
        plt.savefig("static/images/plots/plot9.png")