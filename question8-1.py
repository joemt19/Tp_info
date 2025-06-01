# MBANGA TSHIBANDA ---PREPOLYTECHNIQUE UNIKIN---
# TRAVAIL PRATIQUE D'INFORMATIQUE N°1
# QUESTION 8 PARTIE 1

import multiprocessing
import time

# Calcul CPU-bound : vérifier si un nombre est premier
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(limit):
    count = 0
    for i in range(limit):
        if is_prime(i):
            count += 1
    return count

def multiprocessing_test():
    start = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(count_primes, [100_000, 100_000, 100_000, 100_000])

    end = time.time()
    print(f"[Multiprocessing] Temps total : {end - start:.2f} secondes")

if __name__ == "__main__":
    multiprocessing_test()
    