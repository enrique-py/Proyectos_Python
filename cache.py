""""Se define una funcion cache que guarda y recupera los argumentos que se le pasan a la funcion"""
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

# se ejecuta una funcion que consume altos recursos de maquina
@cache 
def fib(arg1):
    if arg1 <= 1:
        return arg1
    else:
        result = fib(arg1-1) + fib(arg1-2)
        return result
    
fib(100)