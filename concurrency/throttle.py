from threading import Lock
import time

class Throttle:
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0
        self.last = 0

    def consume(self, amount=1):
        with self._consume_lock:
            now = time.time()
            if self.last == 0:
                self.last = now

            elapsed = now - self.last

            if int(elapsed * self.rate):
                self.tokens += int(elapsed * self.rate)
                self.last = now

            self.tokens = (
                self.rate
                if self.tokens > self.rate
                else self.tokens
            )

            if self.tokens >= amount:
                self.tokens -= amount
            else:
                amount = 0

            return amount

import time
from queue import Queue,Empty
from threading import Thread

import requests,random

THREAD_POOL_SIZE = 4

SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')

def fetch_rates(base):
    response = requests.get(
        f"https://api.exchangeratesapi.io/latest?base={base}"
    )
    if random.randint(0, 5) < 1:
        response.status_code = 429
    response.raise_for_status()
    rates = response.json()['rates']

    rates[base] = 1.
    return base, rates

def present_result(base,rates):
    rates_line = ", ".join(
        [f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS]
    )
    print(f"1 {base} = {rates_line}")

def worker(work_queue,results_queue,throttle):
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            while not throttle.consume():
                pass
            try:
                result = fetch_rates(item)
            except Exception as err:
                results_queue.put(err)
            else:
                results_queue.put(result)
            finally:
                work_queue.task_done()

def main():
    work_queue = Queue()
    results_queue = Queue()
    throttle = Throttle(10)

    for base in BASES:
        work_queue.put(base)

    threads = [
        Thread(target=worker,args=(work_queue,results_queue, throttle))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()

    while not results_queue.empty():
        result = results_queue.get()
        if isinstance(result,Exception):
            raise result
        present_result(*result)

if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("time elapsed: {:.2f}s".format(elapsed))

