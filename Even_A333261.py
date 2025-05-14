import sys
import time
from sympy import divisors
from functools import lru_cache

# --- Logger Setup ---
class Logger:
    def __init__(self, filename="results_log.txt"):
        self.terminal = sys.stdout
        self.log = open(filename, "a", buffering=1)  # Line-buffered

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger()  # Redirect stdout to both terminal and file

# --- Begin main logic ---
start_time = time.time()  # Start tracking time

cached_divisors = lru_cache()(divisors)

def A071324(n):
    return sum(d if i % 2 == 0 else -d for i, d in enumerate(reversed(cached_divisors(n))))

def candidates_analysis(n):
    if n % 30 == 24 or n % 12 == 8 or n % 30 == 20:
        return True
    else:
        return False

def mod_check(n):
    if n % 30 == 24:
        return "n = 24 (mod 30)"
    elif n % 12 == 8:
        return "n = 8 (mod 12)"
    elif n % 30 == 20:
        return "n = 20 (mod 30)"

# Main search loop
count = 0
number_of_results = 0

for n in range(11613999978, (10**15) + 2, 2):  # Even numbers only
    count += 1
    if candidates_analysis(n):
        if A071324(n) == A071324(n + 1):
            print("Result! n =", n,
                  "A071324(n) =", A071324(n),
                  "Modular relation -", mod_check(n))
            number_of_results += 1
    # Progress report
    if count % 10**6 == 0:
        elapsed = time.time() - start_time
        print("Checked up to n =", n,
              "Time elapsed (sec):", round(elapsed, 2),
              "Number of results:", number_of_results)

###################
# A computational search for even n > 2 such that A071324(n) = A071324(n+1),
# starting from the biggest such term known. We apply results from our paper, see candidate analysis function.
