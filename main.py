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
    limiter = request.form["num_results"]

    # Connect to MySQL
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE')}"
    )

    # Connect to database
    with engine.connect() as connection:
        # Execute query for most recent update
        total_cases = (
            connection.execute(
                text(
                    "SELECT total_cases, date, positive_rate "
                    "FROM covid_data "
                    f"WHERE iso_code = '{country}' "
                    f"LIMIT {limiter}"
                )
            )
            .mappings()
            .all()
        )
    return render_template("total_cases.html", data=total_cases)


@app.route("/outcomes", methods=["GET"])
def outcomes_form():
    return render_template("outcomes_form.html")


# make a new page
@app.route("/outcomes", methods=["POST"])
def outcome():
    country = request.form["country_filter"]
    limiter = request.form["num_results"]

    # Connect to MySQL
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE')}"
    )

    # Connect to database
    with engine.connect() as connection:
        # Execute query for most recent update
        outcomes = (
            connection.execute(
                text(
                    "SELECT hosp_patients, icu_patients, total_deaths, date "
                    "FROM covid_data "
                    f"WHERE iso_code = '{country}' "
                    f"LIMIT {limiter}"
                )
            )
            .mappings()
            .all()
        )
    return render_template("outcomes.html", data=outcomes)


@app.route("/vaccination_status", methods=["GET"])
def vaccination_status_form():
    return render_template("vaccination_status_form.html")


# make a new page
@app.route("/vaccination_status", methods=["POST"])
def vax_status():
    country = request.form["country_filter"]
    limiter = request.form["num_results"]

    # Connect to MySQL
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE')}"
    )

    # Connect to database
    with engine.connect() as connection:
        # Execute query for most recent update
        vaccinations = (
            connection.execute(
                text(
                    "SELECT total_vaccinations, total_boosters, date "
                    "FROM covid_data "
                    f"WHERE iso_code = '{country}' "
                    f"LIMIT {limiter}"
                )
            )
            .mappings()
            .all()
        )
    return render_template("vaccination_status.html", data=vaccinations)
