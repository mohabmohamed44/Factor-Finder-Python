<<<<<<< HEAD
import math, sys

print('Factor finder a number factors are 2 numbers that, when multiplied with each other, produce the number')

while True: #Main Program loop
    print('Enter a positive whole number to factor (or QUIT): ')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()
    
    if not(response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of number
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    # Convert to a set to get rid of duplicate factors:
    factors = list(set(factors))
    factors.sort()

    # Display the results:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))
=======
import math, sys
print('Factor finder a number factors are 2 numbers that, when multiplied with each other, produce the number')

while True:
    print('Enter a positive whole number to factor (or QUIT): ')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()
    if not(response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of number
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    # Convert to a set to get rid of duplicate factors:
    factors = list(set(factors))
    factors.sort()

    # Display the results:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))

>>>>>>> 0ed4f3f3e8b77e1c526a11c7ebf7b5dc6efcf125
