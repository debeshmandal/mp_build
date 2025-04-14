import multiprocessing as mp
import os
from softnanotools.logger import Logger
logger = Logger(__name__)

def job(x):
    return x * x

def run():
    if os.name == 'nt':
        logger.error("Windows is not supported", exc_info=True)
    results = []
    with mp.get_context("fork").Pool(mp.cpu_count()) as pool:
        results = pool.map(job, range(10))
    return results

if __name__ == "__main__":
    run()
