from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    hw = "hello world!"
    return render_template("home.html", hw=hw)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)