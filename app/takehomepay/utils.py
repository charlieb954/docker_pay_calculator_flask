def thousands_format(num):
    return f"{num:,.2f}"


def thousands_to_float(thousands):
    return float(thousands.replace(",", ""))
