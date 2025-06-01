# MBANGA TSHIBANDA ---PREPOLYTECHNIQUE UNIKIN---
# TRAVAIL PRATIQUE D'INFORMATIQUE N°1
# QUESTION 8 PARTIE 2

import threading
import time

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

def threading_test():
    start = time.time()
    threads = []

    for _ in range(4):
        t = threading.Thread(target=count_primes, args=(100_000,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print(f"[Threading] Temps total : {end - start:.2f} secondes")

if __name__ == "__main__":
    threading_test()
