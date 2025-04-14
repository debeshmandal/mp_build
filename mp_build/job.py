import multiprocessing as mp

def job(x):
    return x * x

def run():
    results = []
    with mp.get_context("fork").Pool(mp.cpu_count()) as pool:
        results = pool.map(job, range(10))
    return results

if __name__ == "__main__":
    run()
