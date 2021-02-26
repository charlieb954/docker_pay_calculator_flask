__all__ = ['tax_pens_20',
        'national_insurance_20']

def tax_pens_20(sal, pens):
    """
    calulate tax contributions for 2020-21 tax year.
    
    parameters
    ----------
    sal = int: salary
    pens = int: pension contribution as a percentage

    returns
    -------
    str: total_tax to pay, str: pension_contr to pay
    """
    pension_contr = sal * (pens/100)
    allowance = 12500
    sal = sal - pension_contr

    if sal <= allowance:
        return str("%.2f" %0), str("%.2f" %pension_contr)

    elif sal in range(12501,50001):
        tax1 = 0 * allowance
        tax2 = 0.2 * (sal - allowance)
        total_tax = tax1 + tax2
        return str("%.2f" %total_tax), str("%.2f" %pension_contr)

    elif sal in range(50001,100001):
        tax1 = 0 * allowance
        tax2 = 0.2 * 37500
        tax3 = 0.4 * (sal - 50000)
        total_tax = tax1 + tax2 + tax3
        return str("%.2f" %total_tax), str("%.2f" %pension_contr)

    elif sal in range(100001,125000):
        allowance = (sal - 100000) / 2
        tax1 = 0.2 * 37500
        tax2 = 0.4 * (sal - (37500 + allowance))
        total_tax = tax1 + tax2
        return str("%.2f" %total_tax), str("%.2f" %pension_contr)

    elif sal in range(125000,150001):
        tax1 = 0.2 * 37500
        tax2 = 0.4 * (sal - 37500)
        total_tax = tax1 + tax2
        return str("%.2f" %total_tax), str("%.2f" %pension_contr)

    elif sal >= 150001:
        tax1 = 0.2 * 37500
        tax2 = 0.4 * 112500
        tax3 = 0.45 * (sal - 150000)
        total_tax = tax1 + tax2 + tax3
        return str("%.2f" %total_tax), str("%.2f" %pension_contr) 
    
    else:
        return 'Unknown'

def national_insurance_20(sal):
    """
    calulate national insurance contributions for 2020-21 tax year.
    
    parameters
    ----------
    sal = int: salary

    returns
    -------
    str: weekly national insurance payment
    """
    weekly = sal / 52

    if int(weekly) in range(0, 184):
        ni = 0
        return str("%.2f" %ni)

    elif int(weekly) in range(184, 963):
        ni = (weekly - 183) * 0.12
        return str("%.2f" %ni)

    elif int(weekly) > 962:
        ni = (779 * 0.12) + ((weekly - 779 - 183) * 0.02)
        return str("%.2f" %ni)

    else:
        return 'Unknown'