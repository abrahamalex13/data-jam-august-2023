import pathlib
import sqlite3

DIR_DATA_DB = pathlib.Path("./data/BikeShareTrips/processed")
con = sqlite3.connect(DIR_DATA_DB / "houston-b-cycle.db")