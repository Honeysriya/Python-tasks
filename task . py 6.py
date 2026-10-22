def rate_per_litre(fat, snf):
    rate = 30 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30
    return round(rate, 2)

def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total():
    total = 0

    for i in range(10):
        litres = float(input("Litres: "))
        fat = float(input("Fat: "))
        snf = float(input("SNF: "))
        total += payout(litres, fat, snf)

    return round(total, 2)

print("Total payment:", ten_day_total())