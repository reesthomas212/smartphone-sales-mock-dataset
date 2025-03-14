from tables.products import Products
from tables.regions import Regions
from tables.channels import Channels
from tables.sales import Sales

"""

Goal: Create a mock "Smartphone Sales" dataset that mimics 
typical real-world sales data variance as much as possible.

Context: Smartphone resellers sell used smartphones across the globe and 
wants to analyze sales performance, regional demand, and product popularity.

"""


def main():

    # Orchestrate table creation and export.
    t1 = Products()
    t2 = Regions()
    t3 = Channels()
    t4 = Sales()

    t1_data = t1.create()
    t2_data = t2.create()
    t3_data = t3.create()
    t4.create(t1_data, t2_data, t3_data)

    t1.export_to_csv()
    t2.export_to_csv()
    t3.export_to_csv()
    t4.export_to_csv()


if __name__ == "__main__":
    main()
