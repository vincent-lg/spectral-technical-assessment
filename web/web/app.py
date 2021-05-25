"""Flask main app.

Entrypoints are defined here and in the 'blueprints' package for the API.

"""

from flask import Flask, g, render_template

from blueprints.api import api, collect

app = Flask(__name__)
app.config.from_object("settings")
app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def index():
    req = collect()
    return render_template("index.html", steps=req.json)
