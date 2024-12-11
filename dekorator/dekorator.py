def logger(func):
    def wrapper(*args):
        print(f"Calling function {func.__name__}")
        result = func(*args)
        print(f"Function {func.__name__} returned: \n{result}")
        return result
    return wrapper

@logger
def Upper(x):
    return x.upper()

Upper('Jakub Wiacek')