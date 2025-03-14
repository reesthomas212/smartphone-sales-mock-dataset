import pandas as pd
from static_data import channels


class Channels:

    """

    Channels Dataset Module
    ---------------
    GOAL: Assemble this table of sales channels data based on AI-generated static data.

    """

    def __init__(self, filename: str = "csv/channels.csv"):
        self.filename = filename
        self.data = None

    def create(self) -> pd.DataFrame:
        self.data = pd.DataFrame(channels)
        return self.data

    def export_to_csv(self) -> None:
        if self.data is None:
            raise ValueError("Table data not created yet.")
        self.data.to_csv(self.filename, index=False)

    def __str__(self) -> str:
        # Return a string representation of the table.
        return f"Channels: {self.data.to_string() if self.data is not None else 'Not created'}"
