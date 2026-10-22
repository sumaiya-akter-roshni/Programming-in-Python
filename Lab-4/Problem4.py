total = 0

for number in range(2, 1000):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
    if is_prime:
        total = total + number

print("Sum of primes below 1000 =", total)