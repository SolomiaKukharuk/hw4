def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
<<<<<<< Updated upstream
=======
def is_power_of_five(n):
    if n == 1:
        return True
    if n < 1 or n % 5 != 0:
        return False
    return is_power_of_five(n/5)

print(is_power_of_five(125))
def is_power_of_two(n):
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n/2)
>>>>>>> Stashed changes
