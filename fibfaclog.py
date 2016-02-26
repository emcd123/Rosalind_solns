def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

def factorial_log(n):
    print("-> factorial({})".format(n))
    res = 1
    for i in range(1,n+1):
        res = res * i
    print("<- factorial: {}".format(res))
    return res



def factorial2(n):
    if n == 1:
        return 1
    else:
        res = n * factorial2(n-1)
        return res

def factorial2_log(n):
    print("-> factorial2({})".format(n))
    if n == 1:
        print("<- factorial2: 1")
        return 1
    else:
        res = n * factorial2(n-1)
        print("factorial2: {}".format(res))
        return res



def fibonacci(n):
    new, old = 1, 0
    for i in range(n-1):
        new, old = new + old, new
    return new

def fibonacci2(n):
    if n in [1,2]:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)
def fibonacci_log(n):
    print("-> fibonacci({})".format(n))
    new, old = 1, 0
    for i in range(n-1):
        new, old = new + old, new
    print("<- fibonacci: {}".format(new))
    return new

# this function makes a function into a logging function

def log_wrap(f):
    # make new function wrapped_f
    def wrapped_f(*n):
        print("-> {0}({1})".format(f.__name__, n))
        res = f(*n)
        print("<- {0}: {1}".format(f.__name__, res))
        return res
    return wrapped_f

def twoparams(x,y):
    return 2*x - 3*y


# now we could define a logging version of any function
# by
# f_log = log_wrap(f)

