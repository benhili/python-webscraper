import flask
import json
import mongohelper

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def index():
    return "This site is for accessing scraped guardian articles."


@app.route("/intext", methods=["POST"])
def intext():
    search_term = json.loads(flask.request.data)["searchterm"]
    results = mongohelper.find_intext(search_term)
    return results


app.run()
