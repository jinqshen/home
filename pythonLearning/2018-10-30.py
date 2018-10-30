class Student(object):
    def __init__(self, name, age, score):
        __slots__ = ('name', 'age')
        self.__name = name
        self.__age = age
        self.__score = score
    #类似与toString()
    def __str__(self):
        return "Student:%s %d %d" % (self.__name, self.__age, self.__score)
 
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    __repr__ = __str__

s = Student('jinqshen', 22, 88)
print(s)
s
s.age = 23
s.name = 'jinqiangshen'
print(s)
s
s.score = 89
print(s)
s

class Fib(object):
    #初始化
    def __init__(self):
        self.__a, self.__b = 0, 1
    #迭代对象
    def __iter__(self):
        return self
    #迭代时调用next方法
    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a >= 10000:
            raise StopIteration()
        return self.__a
    #像list那样取出元素,传入的参数可为整数，也可能是切片对象slice
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    #未找到属性时调用，可返回值，也可返回函数，不过调用方式不同
    def __getattr__(self, attr):
        if attr == 'address':
            return 'MeiShan SiChuan'
        if attr == 'school':
            return lambda : 'hfut'

for i in Fib():
    print(i)

f = Fib()
print(f[4])

P = f[1 : 5]
print(P)

print(f.address)
print(f.school())
#动态__getattr__,写出链式调用,可以实现url的各种重组
class Chain(object):
    def __init__(self, path = ''):
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__

print(Chain().jinqshen.shop.admin.login)

