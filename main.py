from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    # Pretend data
    most_recent_update = "Feb 11 2024"

    return render_template("landing_page.html",
                           most_recent_update=most_recent_update)
