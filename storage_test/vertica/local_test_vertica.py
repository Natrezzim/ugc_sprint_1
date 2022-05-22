import time
import vertica_python

from test_vertica import (
    create_test_table,
    generate_data_to_table,
    get_sample_query,
    get_insert_query,
    group_elements,
)

ROWS_NUMS = 10000000
CHUNK_SIZE = 5000
CONNECTION = {
    'host': 'localhost',
    'port': 5433,
    'user': 'dbadmin',
    'password': '',
    'database': 'docker',
    'autocommit': True,
    'read_timeout': 600,
    'unicode_error': 'strict',
    'ssl': False
}

def query_time(query_type: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.monotonic()

            res = func(*args, **kwargs)

            query_time_result = time.monotonic() - start_time
            print(f"Query type {query_type}, query_time {query_time_result}")

            return res

        return wrapper

    return decorator


def vertica_test() -> None:

    @query_time("INSERT")
    def insert_to_vertica() -> None:
        with vertica_python.connect(**CONNECTION) as conn:
            cur = conn.cursor()
            for chunk in group_elements(generate_data_to_table(ROWS_NUMS), CHUNK_SIZE):
                cur.executemany(
                    get_insert_query(),
                    chunk,
                    use_prepared_statements=False
                )

    @query_time("SELECT")
    def select_from_vertica() -> None:
        with vertica_python.connect(**CONNECTION) as conn:
            cur = conn.cursor()
            for i in range(CHUNK_SIZE):
                cur.execute(get_sample_query())

    create_test_table(CONNECTION)

    insert_to_vertica()

    select_from_vertica()


if __name__ == "__main__":
    vertica_test()
