from flask import Flask, render_template, request, url_for, jsonify, flash
from takehomepay import national_insurance_20, tax_pens_20
from takehomepay.utils import thousands_format, thousands_to_float
from metrics import record_metrics

app = Flask(__name__)

@app.route('/')
def home(error=None):
    return render_template("home.html", 
                            error=error)

@app.route('/', methods=['POST'])
def my_form_post():
    record_metrics()
    try:
        salary = int(request.form['salary'])
    except ValueError:
        return render_template("home.html", error="Please check your input and try again.") 

    salary_year = salary
    salary_month = salary / 12
    salary_week = salary / 52
    salary_day = salary / 365

    try:
        pension = int(request.form['pension'])
    except:
        pension = 0

    tax_year, pension_year = tax_pens_20(salary, pension)

    tax_month = tax_year / 12
    tax_week = tax_year / 52
    tax_day = tax_year / 365

    pension_month = pension_year / 12
    pension_week = pension_year / 52
    pension_day = pension_year / 365

    ni_week = national_insurance_20(salary)
    ni_year = ni_week * 52
    ni_month = (ni_week * 52) / 12
    ni_day = ni_week / 7

    take_home_year = salary_year - tax_year - pension_year - ni_year
    take_home_month = salary_month - tax_month - pension_month - ni_month
    take_home_week = salary_week - tax_week - pension_week - ni_week
    take_home_day = salary_day - tax_day - pension_day -  ni_day


    return render_template('results.html',
                            salary_year = thousands_format(salary_year),
                            salary_month = thousands_format(salary_month),
                            salary_week = thousands_format(salary_week),
                            salary_day = thousands_format(salary_day),
                            pension_year = thousands_format(pension_year),
                            pension_month = thousands_format(pension_month),
                            pension_week = thousands_format(pension_week),
                            pension_day = thousands_format(pension_day),
                            tax_year = thousands_format(tax_year),
                            tax_month = thousands_format(tax_month),
                            tax_week = thousands_format(tax_week),
                            tax_day = thousands_format(tax_day),
                            ni_year = thousands_format(ni_year),
                            ni_month = thousands_format(ni_month),
                            ni_week = thousands_format(ni_week),
                            ni_day = thousands_format(ni_day),
                            take_home_year = thousands_format(take_home_year),
                            take_home_month = thousands_format(take_home_month),
                            take_home_week = thousands_format(take_home_week),
                            take_home_day = thousands_format(take_home_day))

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
