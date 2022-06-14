import random

resultat = [0,0,0,0,0,0]
antal = 1000

for num in range(antal):
    dice = random.randint(1,6)
    resultat[dice-1] += 1

print(resultat)
for i in range(6):
    print(resultat[i]/antal*100)
