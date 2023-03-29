# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

import math

def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

allvariants = combinations(15, 3) 
print(f"Общее число исходов для 3 деталей = {allvariants}")

succesVariants = combinations(9, 3)
print(f"Общее число благоприятных исходов для 3 деталей (все 3 окрашены) = {succesVariants}")

result = succesVariants/ allvariants *100

print(f"вероятность того, что все извлеченные детали окрашены = {result}")