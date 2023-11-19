from flask import Flask, app, request, render_template
from make import a
app = Flask(__name__, static_folder="result")


@app.route("/")
def hello_world():
    a()
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=30000)
