import time
import requests
from threading import Thread

SYMBOLS = ('USD','EUR','PLN','NOK','CZK')
BASES = ('USD','EUR','PLN','NOK','CZK')

def fetch_rates(base):
    response = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}")
    response.raise_for_status()
    rates = response.json()["rates"]
    rates[base] = 1.

    rates_line = ', '.join(
        [f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")

def main1():
    for base in BASES:
        fetch_rates(base)

def main():
    threads = []
    for base in BASES:
        thread = Thread(target=fetch_rates,args=[base])
        thread.start()
        threads.append(thread)

    while threads:
        threads.pop().join()

if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))