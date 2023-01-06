# some discrete math basics

def binom(n, k):
    div = factorial(k) * factorial(n - k)
    return round(factorial(n) / div)

def prime(n):
    if n < 1:
        return False
    if n == 1 or n == 2:
        return True
    for div in range(2, ceil(sqrt(n)) + 1):
        if n % div == 0:
            return False
    return True

import string

def digit(value):
    if value < 10:
        return str(value)
    else: # a = 10, b = 11, c = 12, etc.
        return string.ascii_lowercase[value - 10]
    
def convert(decimal, base): # convertir un value decimal a otra base
    power = 0
    while base**power <= decimal:
        power += 1
    digits = ''
    pending = decimal
    while power > 0:
        power -= 1
        howmuch = base**power
        digits += digito(pending // howmuch) # las veces que cabe indica el digito
        pending %= howmuch # lo que sobra se cubre con las powers menores
    assert decimal == int(digits, base)
    return digits

def gcd(a, b):
    if b == 0:
        return a
    else:
        g = max(a, b)
        l = min(a, b)
        return gcd(l, g % l)

def fibo(n): # from F_0 up to F_n
    f = [0, 1] 
    while len(f) <= n:
        f.append(f[-1] + f[-2])
    return f
