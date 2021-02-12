from flask import Flask, render_template, request, url_for, jsonify, flash

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
    salary_week = str("%.2f" %(salary/52))
    salary_day = str("%.2f" %(salary/365))

    try:
        pension = int(request.form['pension'])
    except:
        pension = 0

    tax_year, pension_year = tax_pens(salary, pension)

    tax_month = str("%.2f" %(float(tax_year) / 12))
    tax_week = str("%.2f" %(float(tax_year) / 52))
    tax_day = str("%.2f" %(float(tax_year) / 365))

    pension_month = str("%.2f" %(float(pension_year) / 12))
    pension_week = str("%.2f" %(float(pension_year) / 52))
    pension_day = str("%.2f" %(float(pension_year) / 365))

    ni_week = national_insurance(salary)
    ni_year = str("%.2f" %(float(ni_week)*52))
    ni_month = str("%.2f" %((float(ni_week)*52)/12))
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

#current tax year, 19/20
def tax_pens(sal, pens):
    pension_contr = sal * (pens/100)
    sal = sal - pension_contr
    if sal <= 12500:
        return str("%.2f" %0), str("%.2f" %pension_contr)
    elif sal in range(12501,50000):
        tax1 = 0 * 12500
        tax2 = 0.2 * (sal - 12500)
        total_tax = tax1 + tax2
        return str("%.2f" %total_tax), str("%.2f" %pension_contr)
    elif sal in range(50000,100000):
        tax1 = 0 * 12500
        tax2 = 0.2 * 37500
        tax3 = 0.4 * (sal - 50000)
        total_tax = tax1 + tax2 + tax3
        return str("%.2f" %total_tax), str("%.2f" %pension_contr)
    else:
        return 'Unknown, calculator only works up to £100,000'

def national_insurance(sal):
    weekly = sal / 52
    if int(weekly) in range(0, 166):
        ni = 0
        return str("%.2f" %ni)
    elif int(weekly) in range(166, 962):
        ni = (weekly - 166) * 0.12
        return str("%.2f" %ni)
    else:
        ni = (796 * 0.12) + ((weekly - 796 - 166)*0.2)
        return str("%.2f" %ni)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
