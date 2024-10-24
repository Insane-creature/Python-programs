def prime_number(n):
    if n < 2: 
        return "Not Prime"
    if n % 2 == 0:
        return "Not Prime"
    else:
        return "Prime"
    
print(prime_number(2))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]
