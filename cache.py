def cache(func):
    results = {}
    def wrapper(*args):
        if args in results:
            return results[args]
        else:
            result = func(*args)
            results[args] = result
            return result
    return wrapper

@cache 

def expensive_function(n):
    if n in cache:
        return cache[n]
    elif n <= 1:
        return n
    else:
        result = expensive_function(n-1) + expensive_function(n-2)
        cache[n] = result
        return result
    