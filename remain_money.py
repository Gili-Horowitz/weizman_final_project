import math




def remain_cart(money_scanned, money_cart):
    money_scanned=float(money_scanned)
    if(money_scanned<money_cart):
        p = math.ceil((money_cart - money_scanned) * 1000) / 1000
        return f'חסר: {p:.1f} ש"ח'
    elif(money_scanned>=money_cart):
        p = math.ceil((money_scanned - money_cart) * 1000) / 1000
        return f'עודף: {p:.1f} ש"ח'


