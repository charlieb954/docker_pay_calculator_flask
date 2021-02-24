from flask import Flask, render_template, request, url_for, jsonify, flash
from takehomepay import national_insurance_20, tax_pens_20

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/', methods=['POST'])
def my_form_post():
    salary = int(request.form['salary'])
    if salary >= 100000:
        return 'This is only programmed for salaries up to 100k.'
        
    salary_year = str("%.2f" %salary)
    salary_month = str("%.2f" %(salary/12))
    salary_week = str("%.2f" %(salary/(365/7)))
    salary_day = str("%.2f" %(salary/365))

    try:
        pension = int(request.form['pension'])
    except:
        pension = 0

    tax_year, pension_year = tax_pens_20(salary, pension)

    tax_month = str("%.2f" %(float(tax_year) / 12))
    tax_week = str("%.2f" %(float(tax_year) / (365/7)))
    tax_day = str("%.2f" %(float(tax_year) / 365))

    pension_month = str("%.2f" %(float(pension_year) / 12))
    pension_week = str("%.2f" %(float(pension_year) / (365/7)))
    pension_day = str("%.2f" %(float(pension_year) / 365))

    ni_week = national_insurance_20(salary)
    ni_year = str("%.2f" %(float(ni_week)*(365/7)))
    ni_month = str("%.2f" %((float(ni_week)*(365/7))/12))
    ni_day = str("%.2f" %(float(ni_week)/7))

    take_home_year = float(salary_year) - float(tax_year) - float(pension_year) -  float(ni_year)
    take_home_month = float(salary_month) - float(tax_month) - float(pension_month) -  float(ni_month)
    take_home_week = float(salary_week) - float(tax_week) - float(pension_week) -  float(ni_week)
    take_home_day = float(salary_day) - float(tax_day) - float(pension_day) -  float(ni_day)

    take_home_year = str("%.2f" % take_home_year)
    take_home_month = str("%.2f" % take_home_month)
    take_home_week = str("%.2f" % take_home_week)
    take_home_day = str("%.2f" % take_home_day)


    return render_template('results.html',
                            salary_year = salary_year,
                            salary_month = salary_month,
                            salary_week = salary_week,
                            salary_day = salary_day,
                            pension_year = pension_year,
                            pension_month = pension_month,
                            pension_week = pension_week,
                            pension_day = pension_day,
                            tax_year = tax_year,
                            tax_month = tax_month,
                            tax_week = tax_week,
                            tax_day = tax_day,
                            ni_year = ni_year,
                            ni_month = ni_month,
                            ni_week = ni_week,
                            ni_day = ni_day,
                            take_home_year = take_home_year,
                            take_home_month = take_home_month,
                            take_home_week = take_home_week,
                            take_home_day = take_home_day)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
