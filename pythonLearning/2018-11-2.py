#枚举类,是用来定义常量的
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

#unique装饰器检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

#枚举类的多种访问方式
print(Weekday(1), Weekday(1).value)
day1 = Weekday.Sun
print(day1, day1.value)
print(Weekday.Tue.value)

#元类  type()函数可以返回一个对象的类型，也可以创建出新的类型
print(type(day1))

class Student(object):
    def __init__(self, name = 'jinqshen', age = 22):
        self.__name = name
        self.__age = age

    def info(self):
        print('%s : %s' % (self.__name, self.__age))

def fn(self, name = "World"):
    print('Hello %s' % name)

def km(self, value = "ig6b"):
    print('S8 %s' % value)

class RunnableMixln(object):
    def run(self):
        print('Student can run!')
#动态创建类(与静态语言的区别)type(类名, 父类(tuple), 方法(dict))  Python解释器遇到class，扫描class定义的语法，通过type()函数进行定义
Hello = type('Hello', (Student, RunnableMixln), dict(hello = fn, ls = km))  #通过type函数创建Hello class
h = Hello()
h.hello()
h.ls()
h.info()
h.run()

#metaclass(元类)控制类的创建行为
#先创建metaclass，就可以创建类，然后可以创建出实例
#metaclass是类的模板,所以必须从'type'派生

#有点像java里的Class类
class ListMetaclass(type):
    r'''
    @param
    1.当前准备创建的类的对象
    2.类的名字
    3.类继承的父类集合
    4.类的方法集合
    '''
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

class Mylist(list, metaclass = ListMetaclass):
        pass
#Python解释器创建Mylist时，要通过ListMetaclass.__new__()来创建
l = Mylist()
l.add(1)
print(l)

L = list()
#普通的list没有add方法,只有append方法  L.add(1)
L.append(2)
print(L)

#ORM框架  Object Relational Mapping  对象-关系映射   关系数据库的一行映射为一个对象  一个类对应一个table

class Field(object):
    def __init__(self, name, column_type):
        self.__name = name
        self.__column_type = column_type

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.__name)

    @property
    def name(self):
        return self.__name
#由Field派生出IntegerField,StringField等
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  #保存属性与列的映射关系
        attrs['__table__'] = name    #假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print(('ARGS: {}').format(str(args)))
#model:父类,StringField,IntegerField等由ORM框架提供
#剩下的魔术方法如save()方法由metaclass提供
class User(Model):
    #定义类的属性到列的映射:
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')

#创建一个实例
u = User(id = 2015214208, name = 'jinqshen', email = '554695481@qq.com', password = '123456')
#保存到数据库
u.save()
