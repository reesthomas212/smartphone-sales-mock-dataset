import pandas as pd
from numpy import random

"""

--- Sales Fields ---
sale_id - (Integer) (PK) - static
date - (DateTime) - dynamic
product_id - (Integer) - dynamic
region_id - (Integer) - dynamic
channel_id - (Integer) - dynamic
units_sold - (Integer) - dynamic
revenue - (Decimal/Float) ($) - dynamic
discount - (Decimal/Float)

"""


class Sales:

    """Description"""

    # Class-level Constants
    NUM_SALES = 10000
    LAST_DATE = pd.to_datetime("31-12-2024", format="%d-%m-%Y")

    def __init__(self, filename: str = "sales.csv"):
        self.filename = filename
        self.data = None

    def create(self,
               products_data: pd.DataFrame,
               regions_data: pd.DataFrame,
               channels_data: pd.DataFrame) -> pd.DataFrame:

        sale_ids = [i for i in range(1, self.NUM_SALES + 1)]
        dates = self._get_random_dates()
        product_ids, revenues, discounts, units_sold = self.get_sales_data(
            products_data
        )
        region_ids = self._get_random_ids(regions_data)
        channel_ids = self._get_random_ids(channels_data)

        self.data = self._build_dataframe(
            sale_ids,
            dates,
            product_ids,
            region_ids,
            channel_ids,
            revenues,
            discounts,
            units_sold
        )

        return self.data

    def export_to_csv(self) -> None:
        """Export the table to a CSV file."""
        if self.data is None:
            raise ValueError("Table data not created yet.")
        self.data.to_csv(self.filename, index=False)

    def _get_random_dates(self) -> list:
        # Generate a list of random dates between begin_date and end_date.
        # 1. Get 3 dates - start date, end date, and release date from t1_data.
        # 2. In a loop, get a random date between start and end dates.
        # - If the random date isn't after the release date, try again
        # - Otherwise, add the random date to a list of size NUM_SALES.
        # Return that list.

        



        return []

    def _get_random_ids(self, data: pd.DataFrame) -> list:
        # Get a list of random IDs from the given DataFrame.
        return data.sample(n=self.NUM_SALES, replace=True).index.to_list()

    def _get_sales_data(self, t1_data) -> tuple:
        # Generate random, realistic sales data.

        product_ids = []
        revenues = []
        discounts = []
        units_sold = []

        for _ in range(self.NUM_SALES):
            # Randomly select a product ID.
            product_id = t1_data.sample().index[0]
            product_ids.append(product_id)

            # Get the unit price for the product.
            unit_price = t1_data.loc[product_id, 'unit_price']

            # Generate a random number of units sold.
            units = random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                p=[0.8, 0.08, 0.03, 0.03, 0.02,
                   0.01, 0.01, 0.01, 0.005, 0.005]
            )

            # Calculate the discount and revenue.
            discount = random.choice(
                [0, 0.05, 0.1, 0.2],
                p=[0.9, 0.06, 0.03, 0.01])
            revenue = unit_price * units * (1 - discount)
            revenues.append(revenue)
            discounts.append(discount)

        return (product_ids, revenues, discounts, units_sold)

    def _build_dataframe(self, sale_ids: list, dates: list, product_ids: list,
                         region_ids: list, channel_ids: list, units_sold: list,
                         revenues: list, discounts: list) -> pd.DataFrame:

        # Construct the final DataFrame from processed data.
        return pd.DataFrame({
            'sale_id': sale_ids,
            'date': dates,
            'product_id': product_ids,
            'region_id': region_ids,
            'channel_id': channel_ids,
            'units_sold': units_sold,
            'revenue': revenues,
            'discount': discounts
        })

    def __str__(self) -> str:
        """Return a string representation of the table."""
        return f"Table4: {self.data.to_string() if self.data is not None else 'Not created'}"
