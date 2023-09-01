from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home_page():
    return render_template("template.html")


if __name__ == "__main__":
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=True, threaded=True)
