# Importing some modules and setting up a few properties
import sys
import os
import csv
from zipfile import ZipFile
sys.path.append(os.getcwd())
os.environ["DJANGO_SETTINGS_MODULE"] = "tsdb_app.settings"

import django
django.setup()

from core.models import Tag, FundSource, Organization, Strategy, Initiative, SocialPost, Product, Consumer



# Generating BackUp Files (BUF) and zipping them
def main():
    print("Process Started")
    print("................................\n")
    TagBackUp()
    FundSourceBackUp()
    OrganizationBackUp()
    StrategyBackUp()
    InitiativeBackUp()
    SocialPostBackUp()
    ProductBackUp()
    ConsumerBackUp()
    Zipper()
    print("\n................................")
    print("Process successfully completed")



def TagBackUp():
    with open("backupfiles/TagBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["value"])

        if len(Tag.objects.all()) != 0:
            for tag in Tag.objects.all():
                my_writer.writerow([tag.value])
            print("Backed Up Tag table")



def FundSourceBackUp():
    with open("backupfiles/FundSourceBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "location", "email", "site", "funding_possibility", "related_tag"])

        if len(FundSource.objects.all()) != 0:
            for fund_source in FundSource.objects.all():

                all_tags_list = []
                for tag in fund_source.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                my_writer.writerow([fund_source.name, fund_source.location, fund_source.email, fund_source.site, fund_source.funding_possibility, all_tags_str])
            print("Backed Up FundSource table")



def OrganizationBackUp():
    with open("backupfiles/OrganizationBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "location", "category", "email", "site", "status", "funder", "related_tag"])

        if len(Organization.objects.all()) != 0:
            for organization in Organization.objects.all():

                all_funders_list = []
                for fund in organization.funder.all():
                    all_funders_list.append(fund.name)
                all_funders_str = ", ".join(all_funders_list)
                
                all_tags_list = []
                for tag in organization.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                my_writer.writerow([organization.name, organization.location, organization.category, organization.email, organization.site, organization.status, all_funders_str, all_tags_str])
            print("Backed Up Organization table")



def StrategyBackUp():
    with open("backupfiles/StrategyBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "parent_org", "related_tag"])

        if len(Strategy.objects.all()) != 0:
            for strategy in Strategy.objects.all():
                
                all_tags_list = []
                for tag in strategy.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                if not strategy.parent_org:
                    parent = strategy.parent_org
                else:
                    parent = strategy.parent_org.name

                my_writer.writerow([strategy.name, parent, all_tags_str])
            print("Backed Up Strategy table")
    


def InitiativeBackUp():
    with open("backupfiles/InitiativeBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "date", "link", "parent_org", "followed_strategy", "related_tag"])

        if len(Initiative.objects.all()) != 0:
            for initiative in Initiative.objects.all():
                
                all_strategys_list = []
                for strategy in initiative.followed_strategy.all():
                    all_strategys_list.append(strategy.name)
                all_strategys_str = ", ".join(all_strategys_list)

                all_tags_list = []
                for tag in initiative.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                if not initiative.parent_org:
                    parent = initiative.parent_org
                else:
                    parent = initiative.parent_org.name

                my_writer.writerow([initiative.name, initiative.date, initiative.link, parent, all_strategys_str, all_tags_str])
            print("Backed Up Initiative table")



def SocialPostBackUp():
    with open("backupfiles/SocialPostBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["platform", "date", "link", "parent_org", "followed_strategy", "related_tag"])

        if len(SocialPost.objects.all()) != 0:
            for post in SocialPost.objects.all():
                
                all_strategys_list = []
                for strategy in post.followed_strategy.all():
                    all_strategys_list.append(strategy.name)
                all_strategys_str = ", ".join(all_strategys_list)

                all_tags_list = []
                for tag in post.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                if not post.parent_org:
                    parent = post.parent_org
                else:
                    parent = post.parent_org.name

                my_writer.writerow([post.platform, post.date, post.link, parent, all_strategys_str, all_tags_str])
            print("Backed Up SocialPost table")



def ProductBackUp():
    with open("backupfiles/ProductBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "price", "date", "features", "link", "parent_org", "related_tag"])

        if len(Product.objects.all()) != 0:
            for product in Product.objects.all():

                all_tags_list = []
                for tag in product.related_tag.all():
                    all_tags_list.append(tag.value)
                all_tags_str = ", ".join(all_tags_list)

                if not product.parent_org:
                    parent = product.parent_org
                else:
                    parent = product.parent_org.name

                my_writer.writerow([product.name, product.price, product.date, product.features, product.link, parent, all_tags_str])
            print("Backed Up Product table")



def ConsumerBackUp():
    with open("backupfiles/ConsumerBUF.csv", "w", newline="") as wfile:
        my_writer=csv.writer(wfile)
        my_writer.writerow(["name", "email", "age", "location", "social_link"])
        if len(Consumer.objects.all()) != 0:
            for consumer in Consumer.objects.all():
                my_writer.writerow([consumer.name, consumer.email, consumer.age, consumer.location, consumer.social_link])
            print("Backed Up Consumer table")



def Zipper():
    with ZipFile('BUF.zip', "w") as zip_obj:
        zip_obj.write("backupfiles/TagBUF.csv")
        zip_obj.write("backupfiles/FundSourceBUF.csv")
        zip_obj.write("backupfiles/OrganizationBUF.csv")
        zip_obj.write("backupfiles/StrategyBUF.csv")
        zip_obj.write("backupfiles/InitiativeBUF.csv")
        zip_obj.write("backupfiles/SocialPostBUF.csv")
        zip_obj.write("backupfiles/ProductBUF.csv")
        zip_obj.write("backupfiles/ConsumerBUF.csv")
    print("Zipped all BUF files")



if __name__ == "__main__":
    main()