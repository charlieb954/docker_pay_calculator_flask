from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    hw = "hello world!"
    return render_template("home.html", hw=hw)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)