# В лотерее 100 билетов. 
# Из них 2 выигрышных. 
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

import math

def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

allvariants = combinations(100, 2) 
print(f"Общее число сочетаний из 2х билетов = {allvariants}")

print(f"Сочетание из 2х выйгрышных билетов всего одна, поэтому вероятность того, что 2 приобретенных билета окажутся выигрышными  = {100/allvariants} %")