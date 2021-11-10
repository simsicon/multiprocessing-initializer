from sqlalchemy import create_engine

import concurrent.futures


engine = create_engine("postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres?sslmode=disable")

def concurrent_func(a):
    return a + a

if __name__ == '__main__':
    nums = [i for i in range(100)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=2, initializer=engine.dispose) as executor:
            future_to_calculate = {executor.submit(concurrent_func, i) : i for i in nums}

            for future in concurrent.futures.as_completed(future_to_calculate):
                i = future_to_calculate[future]
                val = future.result()
                print(val)