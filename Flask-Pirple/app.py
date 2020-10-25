from flask import flask

app = flask(__name__)


@app.route("/", methods=["Get"])
def home():
    return "Hello World!!"


if __name__ == "__main__":
    app.run()
