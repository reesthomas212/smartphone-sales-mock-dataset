import pandas as pd
from numpy import random


class Sales:

    """

    Sales Dataset Module
    ---------------
    GOAL: Create a table of sales data with random, realistic values.

    """

    # Class-level Constants
    NUM_SALES = 10000
    LAST_DATE = pd.to_datetime("31-12-2024", format="%d-%m-%Y")

    def __init__(self,
                 filename: str = "csv/sales.csv"):
        self.filename = filename
        self.data = None

    def create(self,
               products_data: pd.DataFrame,
               regions_data: pd.DataFrame,
               channels_data: pd.DataFrame) -> pd.DataFrame:

        # Create sales data by field
        sale_ids = [i for i in range(1, self.NUM_SALES + 1)]
        product_ids, dates, units_sold, revenues, discounts = self._create_sales_data(products_data)
        region_ids = self._get_random_ids(regions_data)
        channel_ids = self._get_random_ids(channels_data)

        # Assemble and return a DataFrame using the generated data.
        self.data = pd.DataFrame({
            'sale_id': sale_ids,
            'date': dates,
            'product_id': product_ids,
            'region_id': region_ids,
            'channel_id': channel_ids,
            'units_sold': units_sold,
            'revenue': revenues,
            'discount': discounts
        })

        return self.data

    def export_to_csv(self) -> None:

        # Export the table to a CSV file.
        if self.data is None:
            raise ValueError("Table data not created yet.")
        self.data.to_csv(self.filename, index=False)

    def _get_random_ids(self, data: pd.DataFrame) -> list:

        # Get a list of random IDs from the given DataFrame.
        return random.choice(data['id'], size=self.NUM_SALES).tolist()

    def _create_sales_data(self, products_data) -> tuple:

        # Generate random, realistic sales data.
        product_ids = []
        dates = []
        revenues = []
        discounts = []
        units_sold = []

        for _ in range(self.NUM_SALES):
            # Randomly select a product ID.
            product_id = random.choice(products_data['id'])
            product_ids.append(product_id)

            # Get the unit price for the product.
            unit_price = products_data.loc[products_data['id'] == product_id, 'unit_price'].iloc[0]

            # Generate a random sell date after the product release date.
            release_date = products_data.loc[products_data['id'] == product_id, 'release_date'].iloc[0]
            date = random.choice(
                pd.date_range(
                    pd.to_datetime(
                        release_date, format="%d-%m-%Y"
                    ), self.LAST_DATE
                )
            )
            dates.append(date)

            # Generate a random number of units sold.
            units = random.choice(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                p=[0.8, 0.08, 0.03, 0.03, 0.02,
                   0.01, 0.01, 0.01, 0.005, 0.005]
            )
            units_sold.append(units)

            # Generate a random discount.
            discount = random.choice(
                [0, 0.05, 0.1, 0.2],
                p=[0.9, 0.06, 0.03, 0.01])
            discounts.append(discount)

            # Calculate the revenue using unit price and
            # generated discount and unit values.
            revenue = unit_price * units * (1 - discount)
            revenues.append(revenue)

        return (product_ids, dates, units_sold, revenues, discounts)

    def __str__(self) -> str:
        """Return a string representation of the table."""
        return f"Table4: {self.data.to_string() if self.data is not None else 'Not created'}"
