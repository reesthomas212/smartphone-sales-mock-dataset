import pandas as pd
from static_data import products


class Products:

    """Description"""

    def __init__(self, filename: str = "products.csv"):
        self.filename = filename
        self.data = None

    def create(self) -> pd.DataFrame:
        self.data = pd.DataFrame(products)
        return self.data

    def export_to_csv(self) -> None:
        if self.data is None:
            raise ValueError("Table data not created yet.")
        self.data.to_csv(self.filename, index=False)

    def __str__(self) -> str:
        # Return a string representation of the table.
        return f"Products: {self.data.to_string() if self.data is not None else 'Not created'}"
