a = 7
c = 5
m = 1097 # prime
s = 8
n = 100 # count

x = s
for i in range(n):
    x = (a * x + c) % m
    print(x)

