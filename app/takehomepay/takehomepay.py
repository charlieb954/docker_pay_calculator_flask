from takehomepay.utils import thousands_format

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
    float: total_tax to pay, float: pension_contr to pay
    """
    pension_contr = sal * (pens/100)
    allowance = 12500
    sal = sal - pension_contr

    if sal < 0:
        return 'Unknown'

    elif sal <= allowance:
        total_tax = 0

    elif sal in range(12501,50001):
        tax1 = 0 * allowance
        tax2 = 0.2 * (sal - allowance)
        total_tax = tax1 + tax2

    elif sal in range(50001,100001):
        tax1 = 0 * allowance
        tax2 = 0.2 * 37500
        tax3 = 0.4 * (sal - 50000)
        total_tax = tax1 + tax2 + tax3

    elif sal in range(100001,125000):
        allowance = (sal - 100000) / 2
        tax1 = 0.2 * 37500
        tax2 = 0.4 * (sal - (37500 + allowance))
        total_tax = tax1 + tax2

    elif sal in range(125000,150001):
        tax1 = 0.2 * 37500
        tax2 = 0.4 * (sal - 37500)
        total_tax = tax1 + tax2

    else:
        tax1 = 0.2 * 37500
        tax2 = 0.4 * 112500
        tax3 = 0.45 * (sal - 150000)
        total_tax = tax1 + tax2 + tax3
    
    return total_tax, pension_contr

def national_insurance_20(sal):
    """
    calulate national insurance contributions for 2020-21 tax year.
    
    parameters
    ----------
    sal = int: salary

    returns
    -------
    float: weekly national insurance payment
    """
    weekly = sal / 52

    if int(weekly) < 0:
        return 'Unknown'

    elif int(weekly) in range(0, 184):
        ni = 0

    elif int(weekly) in range(184, 963):
        ni = (weekly - 183) * 0.12

    else:
        ni = (779 * 0.12) + ((weekly - 779 - 183) * 0.02)
 
    return ni