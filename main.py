import os

from flask import Flask, render_template, request
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

    # Add landing_page HTML contents
    page = render_template(
        "landing_page.html", most_recent_update=usa_data_last_update_date
    )

    # Render the page
    return page

@app.route("/total_cases", methods=["GET"])
def total_cases_form():
    return render_template("total_cases_form.html")

# make a new page
@app.route("/total_cases", methods=["POST"])
def total_cases():
    country = request.form["country_filter"]

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
                    f"WHERE iso_code = '{country}' "
                    "LIMIT 30, 10"
                )
            )
            .mappings()
            .all()
        )
    return render_template("total_cases.html", data=us_total_cases)
