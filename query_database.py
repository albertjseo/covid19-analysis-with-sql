import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables from the .env file
load_dotenv()

# Connect to MySQL
engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE')}"
)

# Connect to database
with engine.connect() as connection:
    result = connection.execute(text("select * from covid_data limit 10"))

print(result.mappings().all())
