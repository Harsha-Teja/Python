from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/comedy', methods=['GET'])
def comedy():
    return render_template("comedy.html")


if __name__ == '__main__':
    app.run(port=7000, debug=True)
