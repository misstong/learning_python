import time
from multiprocessing import Pool

import requests


SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR','PLN', 'NOK', 'CZK')

POOL_SIZE = 4

def fetch_rates(base):
    response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}')

    response.raise_for_status()
    rates = response.json()['rates']
    rates[base] = 1.
    return base, rates

def present_result(base, rates):
    rates_line = ','.join(
        [f'{rates[symbol]:7.03} {symbol}' for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")

def main():
    with Pool(POOL_SIZE) as pool:
        results = pool.map(fetch_rates, BASES)

    for result in results:
        present_result(*result)

from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
def main2(use_threads = False):
    if use_threads:
        pool_cls = ThreadPool
    else:
        pool_cls = ProcessPool

    with pool_cls(POOL_SIZE) as pool:
        results = pool.map(fetch_rates, BASES)
    for result in results:
        present_result(*result)
if __name__ == '__main__':
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print('time elapsed: {:.2f}s'.format(elapsed))
