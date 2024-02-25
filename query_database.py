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
    location = connection.execute(text("select distinct location as countries from covid_data where length(iso_code) = 3"))

    # UNITED STATES Queries
    us_data = connection.execute(text("select * from covid_data where iso_code = 'USA' limit 10"))
    us_totalcases = connection.execute(text("select total_cases from covid_data where iso_code = 'USA' limit 30, 10"))
    us_totaldeaths = connection.execute(text("select total_deaths from covid_data where iso_code = 'USA' limit 30, 10"))
    us_icu = connection.execute(text("select icu_patients from covid_data where iso_code = 'USA' limit 30, 10"))
    us_hosp = connection.execute(text("select hosp_patients from covid_data where iso_code = 'USA' limit 30, 10"))
    us_vax = connection.execute(text("select total_vaccinations from covid_data where iso_code = 'USA' limit 30, 10"))
    us_boosted = connection.execute(text("select total_boosters from covid_data where iso_code = 'USA' limit 30, 10"))
    # CANADA Queries
    can_data = connection.execute(text("select * from covid_data where iso_code = 'CAN' limit 10"))
    can_totalcases = connection.execute(text("select total_cases from covid_data where iso_code = 'CAN' limit 30, 10"))
    can_totaldeaths = connection.execute(text("select total_deaths from covid_data where iso_code = 'CAN' limit 30, 10"))
    can_icu = connection.execute(text("select icu_patients from covid_data where iso_code = 'CAN' limit 30, 10"))
    can_hosp = connection.execute(text("select hosp_patients from covid_data where iso_code = 'CAN' limit 30, 10"))
    can_vax = connection.execute(text("select total_vaccinations from covid_data where iso_code = 'CAN' limit 30, 10"))
    can_boosted = connection.execute(text("select total_boosters from covid_data where iso_code = 'CAN' limit 30, 10"))



print(result.mappings().all())
print(location.mappings().all())
print(us_data.mappings().all())
print(can_data.mappings().all())
print(us_totalcases.mappings().all())
print(can_totalcases.mappings().all())
print(us_totaldeaths.mappings().all())
print(can_totaldeaths.mappings().all())
print(us_icu.mappings().all())
print(can_icu.mappings().all())
print(us_hosp.mappings().all())
print(can_hosp.mappings().all())
print(us_vax.mappings().all())
print(can_vax.mappings().all())
print(us_boosted.mappings().all())
print(can_boosted.mappings().all())