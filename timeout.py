import concurrent.futures

class TimeoutException(Exception):
    pass

def timeout(seconds=300, error_message="Timeout"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(func, *args, **kwargs)
                try:
                    return future.result(timeout=seconds)
                except concurrent.futures.TimeoutError:
                    raise TimeoutException(error_message)
        return wrapper
    return decorator
