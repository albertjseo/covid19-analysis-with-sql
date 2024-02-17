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
        # Execute query
        res = connection.execute(text("SELECT iso_code, MAX(date) "
                                      "FROM covid_data "
                                      "WHERE iso_code = 'USA' "
                                      "GROUP BY iso_code "
                                      "ORDER BY iso_code")).mappings().all()

    # Filter for date of last data point for USA
    usa_data_last_update_date = res[0]['max(`date`)']

    return render_template("landing_page.html", most_recent_update=usa_data_last_update_date)
