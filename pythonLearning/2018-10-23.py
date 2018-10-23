def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
#因为返回的函数并没有被立即执行，返回的函数都引用了变量i，所以当变量i的值更新，返回的结果也会更新
#对于返回函数，不要引用任何循环变量或者后面会发生变化的变量
#解决办法，使用函数代替变量
def count_1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count_1()
print(f1(), f2(), f3())
#计数器函数，每次调用返回加一整数
def createCounter():
    #先生成迭代器
    def c():
        i = 0
        while True:
            i = i + 1
            yield i
    k = c()
    def counter():
        return next(k)
    return counter
f = createCounter()
print(f(), f(), f(), f())
#匿名函数
print(list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6])))
r'''
    lambda x : x*x
等价于
    def f(x):
        return x*x;
'''
#匿名函数限制：只能有一个表达式，不用写return，返回值为表达式的结果
#好处：没有名字冲突，匿名函数也是个对象，可用变量赋值调用，也可作为返回值
f = lambda x: x*x
print(f(3))
def build(x, y):
    return lambda : x*y
print(build(3, 4), build(3, 4)())
#装饰器：增强方法，有点类似与java的代理
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2018-10-23')
#相当于执行了now = log(now)
now()
#如果decorator本身需要传入参数，则需要编写一个返回decorater的高阶函数
def log_1(text):
    def decorater(func):
        #保证最终weather.__name__不会变成wrapper
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorater

@log_1('personal define')
def weather():
    print('today, the weather is sunny!')
weather()
#相当于weather = log_1('personal define')(weather)

print(weather.__name__)
#偏函数,用于参数简化
print(int('12345'))
print(int('10101010', base=2))
def int2(x, base=2):
    return int(x, base)

print(int2('10101010'))
int3 = functools.partial(int, base=2)
#functools.partial,设定函数的默认值
print(int3('10101010'))
