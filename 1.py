# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.


# a)
import math

def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

allvariants = combinations(52, 4) 
print(f"Общее число исходов для 4ти карт = {allvariants}")

allClubs = combinations(13, 4) 
print(f"Все крести  для 4ти карт = {allClubs}")

TotalResultA = allClubs / allvariants
print(f"вероятность того, что все карты – крести = {TotalResultA*100}%")

# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

oneAce = combinations(4, 1) 
print(f"количество сочетаний с одним тузом = {oneAce}")

twoAce = combinations(4, 2) 
print(f"количество сочетаний с 2мя тузами = {twoAce}")

threeAce = combinations(4, 3) 
print(f"количество сочетаний с 3 тузами = {threeAce}")

fourAce = combinations(4, 4) 
print(f"количество сочетаний с 4 тузами = {fourAce}")

threeNonAce = combinations(48, 3) 
print(f"количество сочетаний с 3 нетузами = {threeNonAce}")

twoNonAce = combinations(48, 2) 
print(f"количество сочетаний с 2 нетузами = {twoNonAce}")

oneNonAce = combinations(48, 1) 
print(f"количество сочетаний с 1 нетузами = {oneNonAce}")

Blag1Ace = oneAce*threeNonAce
Blag2Ace = twoAce*twoNonAce
Blag3Ace = threeAce*oneNonAce
Blag4Ace = fourAce

Total4Cardscombinations = combinations(52,4)
print(f"количество сочетаний с 4 любыми картами = {Total4Cardscombinations}")

Probability1Ace = Blag1Ace/ Total4Cardscombinations
print(f"Вероятность сочетания с одним тузом = {Probability1Ace*100} %")

Probability2Ace = Blag2Ace/ Total4Cardscombinations
print(f"Вероятность сочетания с 2 тузами = {Probability2Ace*100} %")

Probability3Ace = Blag3Ace/ Total4Cardscombinations
print(f"Вероятность сочетания с 3 тузами = {Probability3Ace*100} %")

Probability4Ace = Blag4Ace/ Total4Cardscombinations
print(f"Вероятность сочетания с 4 тузами = {Probability4Ace*100} %")

TotalProbability = Probability1Ace+Probability2Ace+Probability3Ace+Probability4Ace
print(f"Вероятность сочетания хотя бы 1 тузом  = {TotalProbability*100} %")