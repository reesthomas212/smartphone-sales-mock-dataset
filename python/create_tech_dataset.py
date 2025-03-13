# Goal: Create a mock "Smartphone Sales" dataset that mimics typical real-world sales data variance as much as possible.

# Context: Smartphone resellers sell used smartphones across the globe and wants to analyze sales performance, 
# regional demand, and product popularity.


"""
### Tables ###

--- Sales ---
sale_id - (Integer) (PK)
date - (DateTime)
product_id - (Integer)
region_id - (Integer)
channel_id - (Integer)
units_sold - (Integer)
revenue - (Decimal/Float) ($)

--- Products ---
id - (Integer) (PK)
model_name - (String)
brand - (String)
unit_price - (Decimal/Float) ($)
release_date - (Date)
operating_system
screen_size_inches
display_type
resolution_h

--- Regions ---
id - (Integer) (PK)
country - (String)
continent - (String)
population (M) - (Decimal/Float)
gdp_per_capita - (Integer) ($)
adoption_rate - (Decimal/Float)

--- Channels ---
id - (Integer) (PK)
type - (String)
partner - (String)
resell_cost - (Decimal/Float) ($)
"""

from tables.products import Products
from tables.regions import Regions
from tables.channels import Channels
#from tables.sales import Sales


def main():

    # Orchestrate table creation and export.
    t1 = Products()
    t2 = Regions()
    t3 = Channels()
    #t4 = Sales()

    t1_data = t1.create()
    t2_data = t2.create()
    t3_data = t3.create()
    #t4_data = t4.create(t1_data, t2_data, t3_data)

    t1.export_to_csv()
    t2.export_to_csv()
    t3.export_to_csv()
    #t4.export_to_csv()


if __name__ == "__main__":
    main()


# Order of Events
"""

1. 4 different functions creating 4 different tables
 - Products
 - Regions
 - Channels
 - Sales (Requires data from the previous 3)

"""
