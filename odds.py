
from random import seed
from random import randint

n = int(input("Range?"))

i = 1
j = 1
perm = 0

for i in range(1,(n+1)):

	for j in range(1,(n+1)):

		if((j == i) or ((j+i)==n) ):
			perm += 1

chance = (perm/(n*n))*100
total = n*n

print("")
print("Range: 1 to " + str(n))
print("Permutations where dare has to be executed: " + str(perm))
print("Total permutations: " + str(total))
print("Mathematical Chance of dare being executed: " + str(chance) + "%")

x = 1
num1 = 0
num2 = 0
trueCases = 0
numSimulations = 100000

for x in range(1,numSimulations):
	num1 = randint(1,n)
	num2 = randint(1,n)

	if((num1 == num2) or ((num1 + num2) == n)):
		trueCases += 1

	
simulatedChance = (trueCases/numSimulations)*100

print("Simulated Chance of dare being executed: " + str(simulatedChance) + "%")
print("")



