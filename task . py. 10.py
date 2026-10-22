import time
from decimal import Decimal

for n in [300, 600, 15000]:
    start = time.perf_counter()
    float_total = 0.1 * n
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = Decimal("0.1") * n
    decimal_time = time.perf_counter() - start

    print("Payments:", n)
    print("Float total:", round(float_total, 2))
    print("Decimal total:", decimal_total)
    print("Float time:", round(float_time, 6), "seconds")
    print("Decimal time:", round(decimal_time, 6), "seconds")