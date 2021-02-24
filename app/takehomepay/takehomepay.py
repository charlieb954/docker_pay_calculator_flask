__all__ = ['tax_pens_20',
        'national_insurance_20']

def tax_pens_20(sal, pens):
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

def national_insurance_20(sal):
    weekly = sal / (365/7)
    if int(weekly) in range(0, 184):
        ni = 0
        return str("%.2f" %ni)
    elif int(weekly) in range(184, 962):
        ni = (weekly - 184) * 0.12
        return str("%.2f" %ni)
    else:
        ni = (796 * 0.12) + ((weekly - 796 - 184)*0.2)
        return str("%.2f" %ni)