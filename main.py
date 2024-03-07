import base64
import io
import os

from flask import Flask, render_template, request
from markupsafe import Markup
from matplotlib import axes
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
from sqlalchemy import create_engine, text
from datetime import datetime

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
    return render_template("base.html", content=Markup(page))


@app.route("/total_cases", methods=["GET"])
def total_cases_form():
    page = render_template("total_cases_form.html")

    return render_template("base.html", content=Markup(page))


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

    # reshape data for matplotlib
    dates = []
    case_data = []
    for row in total_cases:
        dates.append(row["date"])

        if row["total_cases"] is None:
            case_values = 0
        else:
            case_values = int(row["total_cases"])
        case_data.append(case_values)

    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Total Cases per Date")
    axis.set_xlabel("Date")
    axis.set_ylabel("Number of Total Cases")
    axis.grid()
    axis.tick_params(direction="out", length=5)
    axis.axes.set_axisbelow(True)

    n = 5
    axis.xaxis.set_major_locator(MultipleLocator(n))
    axis.grid(alpha=0.1, color="black")

    x_data = dates
    y_data = case_data
    axis.plot(x_data, y_data, "b+-")

    total_cases_graph = convert_matplotlib_to_img_src(fig)

    page = render_template(
        "total_cases.html", data=total_cases, total_cases_graph=total_cases_graph
    )

    return render_template("base.html", content=Markup(page))


@app.route("/outcomes", methods=["GET"])
def outcomes_form():
    page = render_template("outcomes_form.html")

    return render_template("base.html", content=Markup(page))


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

    icu_data = []
    death_data = []

    # Generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Total ICU Patients vs Deaths")
    axis.set_xlabel("Total ICU Patients")
    axis.set_ylabel("Total Deaths")
    axis.grid()

    n = 5
    axis.xaxis.set_major_locator(MultipleLocator(n))
    axis.grid(alpha=0.1, color="black")

    x_data = icu_data
    y_data = death_data
    axis.plot(x_data, y_data, "b+-")

    total_outcomes_graph = convert_matplotlib_to_img_src(fig)

    page = render_template(
        "outcomes.html", data=outcomes, total_outcomes_graph=total_outcomes_graph
    )

    return render_template("base.html", content=Markup(page))


@app.route("/vaccination_status", methods=["GET"])
def vaccination_status_form():
    page = render_template("vaccination_status_form.html")

    return render_template("base.html", content=Markup(page))


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


    vax_data = []
    booster_data = []

    for row in vaccinations:
        if row["total_vaccinations"] is None:
            vax_value = 0
        else:
            vax_value = int(row["total_vaccinations"])
        vax_data.append(vax_value)

        if row["total_boosters"] is None:
            booster_value = 0
        else:
            booster_value = int(row["total_boosters"])
        booster_data.append(booster_value)

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Total Vaccinations vs Boosters")
    axis.set_xlabel("Total Vaccinations")
    axis.set_ylabel("Total Boosters")
    axis.grid()

    n = 5
    axis.xaxis.set_major_locator(MultipleLocator(n))
    axis.grid(alpha=0.1, color="black")

    x_data = vax_data
    y_data = booster_data
    axis.plot(x_data, y_data, "b+-")

    total_vaccination_graph = convert_matplotlib_to_img_src(fig)

    page = render_template(
        "vaccination_status.html",
        data=vaccinations,
        total_vaccination_graph=total_vaccination_graph,
    )

    return render_template("base.html", content=Markup(page))


def convert_matplotlib_to_img_src(fig: Figure) -> str:
    """
    Converts a matplotlib Figure into a format passable into an HTML img tag's
    src

    :param fig: matplotlib Figure
    :return:
    """

    # Convert plot to PNG image
    png_image = io.BytesIO()
    FigureCanvas(fig).print_png(png_image)

    # Encode PNG image to base64 string
    png_image_b64_string = "data:image/png;base64,"
    png_image_b64_string += base64.b64encode(png_image.getvalue()).decode("utf8")

    return png_image_b64_string
