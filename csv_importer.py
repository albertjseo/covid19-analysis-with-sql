import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from the .env file
load_dotenv()

# Load data csv
path = "./data.csv"
df = pd.read_csv(path)

# We'll filter for only Canada and United States of America data for now
df = df[(df["iso_code"] == "CAN") | (df["iso_code"] == "USA")]

# Connect to MySQL
engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE')}"
)

# Take the dataframe and create a MySQL table with it
df.to_sql("covid_data", engine)
