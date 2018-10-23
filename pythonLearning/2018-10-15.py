from collections import Iterable
from functools import reduce
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
#生成器
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
#生成器
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
#函数作为参数传入
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, -6, abs))

#map()和reduce()函数
#map接收两个参数：函数，Iterable     将函数依次作用到序列的每个元素
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#reduce  导入，接受两个参数：函数，Iterable   函数必须有两个参数，将函数作用到序列，将结果继续和下一个参数作用
def add_1(x, y):
    return 10 * x + y

print(reduce(add_1, [1, 2, 3, 4]))

num = {'0' : 0, '1' : 1, '2' : 2,  '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def charnum(s):
    return num[s]
print(reduce(add_1, map(charnum, '123456')))

def odd(num):
    return num % 2 == 1

def not_empty(s):
    return s and s.strip()
	
print(list(filter(odd, [1, 2, 4, 5, 6, 7, 9])))
print(list(filter(not_empty, ['A', 'B', '', '', 'C', None,' '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisiable(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n), it)

for i in primes():
    if i < 1000:
        print(i)
    else:
        break
a = 13
print(int(a/10))
