import os

from flask import Flask, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)


@app.route("/")
def main():
    # Connect to MySQL
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE')}"
    )

    # Connect to database
    with engine.connect() as connection:
        # Execute query for most recent update
        most_recent_update = (
            connection.execute(
                text(
                    "SELECT iso_code, MAX(date) "
                    "FROM covid_data "
                    "WHERE iso_code = 'USA' "
                    "GROUP BY iso_code "
                    "ORDER BY iso_code"
                )
            )
            .mappings()
            .all()
        )

        # Filter for date of last data point for USA
        usa_data_last_update_date = most_recent_update[0]["max(`date`)"]

        # Execute query for which countries we have data for
        available_countries = (
            connection.execute(
                text(
                    "SELECT DISTINCT location AS countries "
                    "FROM covid_data "
                    "WHERE length(iso_code) = 3"
                )
            )
            .mappings()
            .all()
        )

    # Add landing_page HTML contents
    page = render_template(
        "landing_page.html", most_recent_update=usa_data_last_update_date
    )

    # Add a table
    page += render_template("countries_table.html", data=available_countries)

    # Render the page
    return page


# make a new page
@app.route("/total_cases")
def total_cases():
    # Connect to MySQL
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE')}"
    )

    # Connect to database
    with engine.connect() as connection:
        # Execute query for most recent update
        us_total_cases = (
            connection.execute(
                text(
                    "SELECT total_cases, date, positive_rate "
                    "FROM covid_data "
                    "WHERE iso_code = 'USA' "
                    "LIMIT 30, 10"
                )
            )
            .mappings()
            .all()
        )
    return render_template("total_cases.html", data=us_total_cases)