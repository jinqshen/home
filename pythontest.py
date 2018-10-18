from collections import Iterable
import os
s = (1,2,3)
d = {'one' : '1', 'two' : '2', 'three' : '3'}
arr = [1,2,3,4]
for ch in 'ABC':
    print(ch)
for key in s:
    print(key)
for k in d:
    print(k)
for v in d.values():
    print(v)
for k,v in d.items():
    print(k, v)
print([k + '=' + v for k,v in d.items()])
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))
array = [(1, 1), (2, 2), (3, 3), (4, 4)]
for x, y in array:
    print(x, y)
L = []
for x in range(1, 10):
    L.append(x * x)
print(L)
print([x * x for x in range(1, 10) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir('.')])
for d in os.listdir('.'):
    print(d)
g = (x * x for x in range(10))
for n in g:
    print(n)
    if(n == 49):
        break


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(6)

def fib_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib_1(5))
for n in fib_1(6):
    print(n)

f = fib_1(4)
print(next(f))
print(next(f))
print(next(f))
print(next(f))


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[k] + L[k + 1] for k in range(len(L) - 1)] + [1]

n = 0
t = triangles()
print("杨辉三角:")
for c in t:
    print(c)
    if n > 10:
        break
    n = n + 1