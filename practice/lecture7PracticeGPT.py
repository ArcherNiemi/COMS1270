import math
import random


# ---------- Primality testing ----------

def is_prime(n):
    if n < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

    for p in small_primes:
        if n % p == 0:
            return n == p

    # Write n - 1 as d * 2^s
    d = n - 1
    s = 0

    while d % 2 == 0:
        s += 1
        d //= 2

    # Deterministic for 64-bit integers
    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

    for a in bases:
        if a % n == 0:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = x * x % n

            if x == n - 1:
                break
        else:
            return False

    return True


# ---------- Pollard's Rho ----------

def pollard_rho(n):
    if n % 2 == 0:
        return 2

    if n % 3 == 0:
        return 3

    while True:
        c = random.randrange(1, n)
        x = random.randrange(0, n)
        y = x
        d = 1

        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n

            d = math.gcd(abs(x - y), n)

        if d != n:
            return d


# ---------- Factorization ----------

def factor(n, result=None):
    if result is None:
        result = []

    if n == 1:
        return result

    if is_prime(n):
        result.append(n)
        return result

    divisor = pollard_rho(n)

    factor(divisor, result)
    factor(n // divisor, result)

    return result


# ---------- Find all factors ----------

def all_factors(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    prime_factors = factor(n)
    prime_factors.sort()

    # Convert prime factors into powers
    powers = []

    i = 0
    while i < len(prime_factors):
        p = prime_factors[i]
        exponent = 0

        while i < len(prime_factors) and prime_factors[i] == p:
            exponent += 1
            i += 1

        powers.append((p, exponent))

    print(powers)

    # Generate all divisors
    divisors = [1]

    for p, exponent in powers:
        new_divisors = []

        for d in divisors:
            value = d

            for _ in range(exponent + 1):
                new_divisors.append(value)
                value *= p

        divisors = new_divisors

    return sorted(divisors)


# ---------- Example ----------

n = 1_000_000_030_020_001_900_012_020_030_000_000_000_000_000_012_000_210_010_000_100_000_000_000_000

f = all_factors(n)

print("Prime factorization:")
print(factor(n))

print("\nNumber of factors:", len(f))

print("\nFactors:")
print(f)
