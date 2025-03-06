# **Python的康复训练**

> 长时间没写 Python，直接让 Claude跑了篇康复训练笔记给我 XD

# **第一章：Python基础语法**

本章主要介绍Python语言的基本语法。熟悉这些基础知识是进行任何编程活动的前提。

## **1.1 变量与数据类型**

在Python中，变量是存储数据的容器。Python是动态类型语言，这意味着我们不需要显式声明变量的类型。

### **1.1.1 基本数据类型**

1. **整数(int)**
```python
a = 5  # 普通整数
b = 0b1010  # 二进制数，值为10
c = 0o12  # 八进制数，值为10
d = 0xA  # 十六进制数，值为10
big_num = 1_000_000  # 使用下划线使大数更易读
```

2. **浮点数(float)**
```python
pi = 3.14159
e = 2.71828
scientific = 3.14e-10  # 科学计数法
```

3. **字符串(str)**
```python
# 字符串可以用单引号或双引号
name = "Python"
message = 'Hello, World!'

# 多行字符串使用三引号
multi_line = """这是第一行
这是第二行
这是第三行"""

# 字符串格式化
name = "Alice"
age = 25
# f-string (推荐)
print(f"My name is {name} and I am {age} years old")
# format方法
print("My name is {} and I am {} years old".format(name, age))
# %操作符
print("My name is %s and I am %d years old" % (name, age))
```

4. **布尔值(bool)**
```python
is_active = True
is_empty = False
# 布尔运算
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

### **1.1.2 类型转换**

Python提供了多种类型转换函数：

```python
# 字符串转换
str_num = "123"
num = int(str_num)      # 字符串转整数: 123
float_num = float(str_num)  # 字符串转浮点数: 123.0

# 数字转字符串
num = 123
str_num = str(num)      # 数字转字符串: "123"

# 检查数据类型
print(type(123))        # <class 'int'>
print(type("hello"))    # <class 'str'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>

# 类型判断
print(isinstance(123, int))        # True
print(isinstance("hello", str))    # True
```

### **1.1.3 变量命名规则**

1. 变量名只能包含字母、数字和下划线
2. 变量名必须以字母或下划线开头
3. 变量名区分大小写
4. 不能使用Python关键字

```python
# 正确的命名
user_name = "Alice"
age1 = 25
_private = "private variable"

# 错误的命名
# 2name = "John"    # 不能以数字开头
# my-name = "Bob"   # 不能使用连字符
# class = "Python"  # 不能使用关键字
```

## **1.2 数据结构**

Python内置了丰富的数据结构，每种数据结构都有其特定的使用场景和优势。

### **1.2.1 列表(List)**

列表是Python中最常用的数据结构之一，它是一个可变的、有序的元素集合。

```python
# 创建列表
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # 列表可以包含不同类型的元素
empty_list = []  # 空列表
list_from_range = list(range(5))  # 使用range创建列表: [0, 1, 2, 3, 4]

# 列表索引和切片
lst = [10, 20, 30, 40, 50]
print(lst[0])       # 第一个元素: 10
print(lst[-1])      # 最后一个元素: 50
print(lst[1:3])     # 切片，获取索引1到2的元素: [20, 30]
print(lst[::2])     # 步长为2: [10, 30, 50]
print(lst[::-1])    # 反转列表: [50, 40, 30, 20, 10]

# 列表常用方法
lst = [1, 2, 3]
lst.append(4)        # 添加元素到末尾: [1, 2, 3, 4]
lst.insert(1, 5)     # 在索引1处插入5: [1, 5, 2, 3, 4]
lst.extend([6, 7])   # 扩展列表: [1, 5, 2, 3, 4, 6, 7]
lst.remove(5)        # 删除第一个值为5的元素
popped = lst.pop()   # 移除并返回最后一个元素
lst.sort()           # 排序（原地排序）
lst.reverse()        # 反转列表
index = lst.index(3) # 获取元素3的索引
count = lst.count(2) # 计算元素2出现的次数

# 列表推导式
squares = [x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]
```

### **1.2.2 元组(Tuple)**

元组是不可变的序列类型，一旦创建就不能修改。

```python
# 创建元组
point = (3, 4)
single_element = (1,)  # 单元素元组必须加逗号
empty_tuple = ()
tuple_from_list = tuple([1, 2, 3])

# 元组解包
x, y = point  # x=3, y=4
a, *rest, b = (1, 2, 3, 4, 5)  # a=1, rest=[2,3,4], b=5

# 元组操作
coordinates = (1, 2) + (3, 4)  # 连接元组: (1, 2, 3, 4)
repeated = (1, 2) * 3          # 重复元组: (1, 2, 1, 2, 1, 2)
exists = 3 in (1, 2, 3)        # 成员检测: True

# 元组方法
tup = (1, 2, 2, 3, 4)
count = tup.count(2)    # 计数：2出现了2次
index = tup.index(3)    # 获取3的索引：3
```

### **1.2.3 集合(Set)**

集合是无序的、不重复元素的集合，支持数学运算。

```python
# 创建集合
numbers = {1, 2, 3, 4, 5}
set_from_list = set([1, 2, 2, 3])  # 重复元素会被去除
empty_set = set()  # 注意：{}创建的是空字典，不是空集合

# 集合操作
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)     # 并集: {1, 2, 3, 4, 5}
print(s1 & s2)     # 交集: {3}
print(s1 - s2)     # 差集: {1, 2}
print(s1 ^ s2)     # 对称差集: {1, 2, 4, 5}

# 集合方法
s = {1, 2, 3}
s.add(4)           # 添加单个元素
s.update([4, 5, 6])# 添加多个元素
s.remove(4)        # 删除元素（元素不存在会报错）
s.discard(4)       # 删除元素（元素不存在不会报错）
popped = s.pop()   # 随机移除并返回一个元素
s.clear()          # 清空集合
```

### **1.2.4 字典(Dictionary)**

字典是键值对的集合，提供了高效的查找机制。

```python
# 创建字典
person = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Java"]
}
dict_from_pairs = dict([("a", 1), ("b", 2)])
empty_dict = {}

# 访问和修改
print(person["name"])              # 访问值：Alice
person["age"] = 26                 # 修改值
person["location"] = "New York"    # 添加新键值对
value = person.get("salary", 0)    # 安全访问，如果键不存在返回默认值0

# 字典方法
keys = person.keys()               # 获取所有键
values = person.values()           # 获取所有值
items = person.items()             # 获取所有键值对
person.update({"salary": 5000})    # 更新或添加多个键值对
popped = person.pop("age")         # 移除并返回指定键的值
person.clear()                     # 清空字典

# 字典推导式
squares = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# 嵌套字典
employees = {
    "emp1": {"name": "John", "salary": 5000},
    "emp2": {"name": "Alice", "salary": 6000}
}
```

## **1.3 控制结构**

Python提供了多种控制结构来控制程序的执行流程。

### **1.3.1 条件语句(if)**

Python使用缩进来标识代码块，条件语句的基本结构如下：

```python
# 基本if语句
age = 20
if age >= 18:
    print("成年人")
elif age >= 12:
    print("青少年")
else:
    print("儿童")

# 条件表达式（三元运算符）
status = "成年" if age >= 18 else "未成年"

# 复合条件
score = 85
is_student = True
if score >= 60 and is_student:
    print("及格")

# 多条件判断
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"

# 成员判断
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("有苹果")

# 身份判断
x = None
if x is None:
    print("x是None")

# 真值判断
# 以下值在条件判断中都被视为False：
# False, None, 0, 0.0, '', [], {}, set()
empty_list = []
if not empty_list:
    print("列表为空")
```

### **1.3.2 for循环**

Python的for循环可以遍历任何可迭代对象。

```python
# 基本for循环
for i in range(5):
    print(i)  # 打印0到4

# 遍历列表
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# 使用enumerate获取索引和值
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 遍历字典
person = {"name": "Alice", "age": 25}
for key in person:
    print(f"{key}: {person[key]}")

# 更pythonic的字典遍历
for key, value in person.items():
    print(f"{key}: {value}")

# 循环嵌套
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # 换行

# 列表推导式中的for
squares = [x**2 for x in range(5)]

# 使用zip同时遍历多个序列
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### **1.3.3 while循环**

while循环在条件为真时重复执行代码块。

```python
# 基本while循环
count = 0
while count < 5:
    print(count)
    count += 1

# 使用while循环处理用户输入
while True:
    response = input("请输入'quit'退出: ")
    if response.lower() == 'quit':
        break
    print(f"你输入了: {response}")

# 带else的while循环
# 当while循环正常结束（不是通过break）时执行else块
number = 0
while number < 3:
    print(number)
    number += 1
else:
    print("循环正常结束")

# 使用while循环实现倒计时
import time
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)  # 暂停1秒
print("发射！")
```

### **1.3.4 循环控制语句**

Python提供了几种控制循环执行的语句。

```python
# break: 立即退出循环
for i in range(10):
    if i == 5:
        break
    print(i)  # 只打印0到4

# continue: 跳过当前迭代
for i in range(5):
    if i == 2:
        continue
    print(i)  # 打印0,1,3,4

# pass: 空操作
for i in range(3):
    if i == 1:
        pass  # 什么都不做
    else:
        print(i)

# 循环中的else子句
# 当循环正常完成（不是通过break退出）时执行
for i in range(3):
    print(i)
else:
    print("循环正常完成")

# 在嵌套循环中使用break和continue
for i in range(3):
    for j in range(3):
        if i == j:
            continue  # 跳过当前内循环迭代
        print(f"({i}, {j})", end=" ")
    print()
```

### **1.3.5 异常处理**

虽然这通常在后面的章节介绍，但基本的异常处理也是控制流的重要部分：

```python
# 基本的try-except结构
try:
    number = int(input("请输入一个数字: "))
    result = 10 / number
    print(f"结果是: {result}")
except ValueError:
    print("输入必须是数字")
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:
    print(f"发生错误: {e}")
else:
    print("计算成功完成")
finally:
    print("无论如何都会执行这里")
```

# **第二章：函数与模块**

## **2.1 函数的定义与调用**

函数是可重用的代码块，它可以接收参数、执行特定任务并返回结果。

### **2.1.1 基本函数定义**

```python
# 基本函数定义
def greet(name):
    """
    向指定的人打招呼
    Args:
        name: 人名
    Returns:
        打招呼的字符串
    """
    return f"Hello, {name}!"

# 调用函数
print(greet("Alice"))  # 输出: Hello, Alice!

# 多返回值
def get_coordinates():
    x = 10
    y = 20
    return x, y  # 实际上返回一个元组

# 解包多返回值
x, y = get_coordinates()
```

### **2.1.2 函数参数**

Python提供了多种参数传递方式：

```python
# 位置参数
def power(base, exponent):
    return base ** exponent

print(power(2, 3))  # 8

# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))          # Hello, Alice!
print(greet("Bob", "Hi"))      # Hi, Bob!

# 关键字参数
def create_profile(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

print(create_profile(age=25, city="Beijing", name="Alice"))

# 可变位置参数 (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # 10

# 可变关键字参数 (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Beijing")

# 混合使用各种参数
def complex_function(pos1, pos2, *args, default="default", **kwargs):
    print(f"位置参数: {pos1}, {pos2}")
    print(f"可变位置参数: {args}")
    print(f"默认参数: {default}")
    print(f"关键字参数: {kwargs}")

complex_function(1, 2, 3, 4, 5, x=10, y=20)
```

### **2.1.3 作用域和命名空间**

```python
# 全局变量和局部变量
global_var = 10

def function():
    local_var = 20
    print(global_var)  # 可以访问全局变量
    print(local_var)   # 局部变量

# global关键字
counter = 0
def increment():
    global counter
    counter += 1
    return counter

# nonlocal关键字（用于嵌套函数）
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

# 闭包示例
def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

## **2.2 高级函数特性**

### **2.2.1 装饰器**

```python
# 基本装饰器
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行时间: {end - start}秒")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "完成"

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")
```

### **2.2.2 生成器**

```python
# 生成器函数
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# 使用生成器
for i in countdown(5):
    print(i)

# 生成器表达式
squares = (x**2 for x in range(10))

# 无限生成器
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

## **2.3 模块和包**

### **2.3.1 模块导入**

```python
# 基本导入
import math
print(math.pi)

# 导入特定内容
from random import randint, choice
print(randint(1, 10))

# 使用别名
import numpy as np
import pandas as pd

# 导入所有内容（不推荐）
from math import *
```

### **2.3.2 创建自己的模块**

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    def add(self, x, y):
        return x + y

# 在其他文件中使用
import mymodule
print(mymodule.greet("Alice"))
```

### **2.3.3 包的结构**

```plaintext
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

```python
# __init__.py 示例
from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']
```

### **2.3.4 常用标准库**

```python
# 日期和时间处理
from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(days=7)

# 文件路径处理
import os.path
path = os.path.join('folder', 'subfolder', 'file.txt')

# JSON处理
import json
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
parsed_data = json.loads(json_str)

# 正则表达式
import re
pattern = r'\d+'
text = "abc123def456"
numbers = re.findall(pattern, text)

# 随机数
import random
random_num = random.randint(1, 100)
random_choice = random.choice(['apple', 'banana', 'orange'])

# 系统相关
import sys
print(sys.version)
print(sys.platform)
```

# **第三章：面向对象编程（OOP）**

## **3.1 类与对象基础**

### **3.1.1 类的定义与实例化**

```python
# 基本类定义
class Person:
    # 类变量（所有实例共享）
    species = "Human"
    
    # 构造方法
    def __init__(self, name, age):
        # 实例变量（每个实例独有）
        self.name = name
        self.age = age
        self._private = None      # 约定私有（单下划线）
        self.__very_private = 0   # 名称改写私有（双下划线）

    # 实例方法
    def greet(self):
        return f"Hello, my name is {self.name}"
    
    # 获取年龄描述
    def get_age_description(self):
        if self.age < 18:
            return "未成年"
        return "成年人"

# 创建实例
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# 访问属性和方法
print(person1.name)          # 访问实例变量
print(Person.species)        # 访问类变量
print(person1.greet())      # 调用方法
```

### **3.1.2 属性装饰器**

```python
class Student:
    def __init__(self):
        self._score = 0

    # 使用property装饰器
    @property
    def score(self):
        return self._score

    # 设置器
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("分数必须是整数")
        if value < 0 or value > 100:
            raise ValueError("分数必须在0-100之间")
        self._score = value

    # 只读属性
    @property
    def grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 80:
            return 'B'
        elif self._score >= 70:
            return 'C'
        else:
            return 'D'

# 使用属性
student = Student()
student.score = 85  # 使用setter
print(student.score)  # 使用getter
print(student.grade)  # 访问只读属性
```

### **3.1.3 静态方法和类方法**

```python
class MathOperations:
    # 类变量
    pi = 3.14159

    def __init__(self, value):
        self.value = value

    # 实例方法（需要实例）
    def double(self):
        return self.value * 2

    # 静态方法（不需要实例）
    @staticmethod
    def is_positive(number):
        return number > 0

    # 类方法（可访问类变量）
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    # 类方法作为替代构造函数
    @classmethod
    def from_string(cls, string_value):
        value = float(string_value)
        return cls(value)

# 使用示例
math_ops = MathOperations(5)
print(math_ops.double())                    # 实例方法
print(MathOperations.is_positive(10))       # 静态方法
print(MathOperations.circle_area(5))        # 类方法
new_ops = MathOperations.from_string("10")  # 替代构造函数
```

## **3.2 继承与多态**

### **3.2.1 基本继承**

```python
# 基类
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")
    
    def introduce(self):
        return f"I am {self.name}, and I can {self.speak()}"

# 子类
class Dog(Animal):
    def speak(self):
        return "woof!"
    
    # 扩展父类方法
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I'm a good boy!"

class Cat(Animal):
    def speak(self):
        return "meow!"

# 使用示例
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.introduce())
print(cat.introduce())
```

### **3.2.2 多重继承**

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "quack!"
    
    def introduce(self):
        return f"{super().introduce()} {self.fly()} {self.swim()}"

# 使用多重继承
duck = Duck("Donald")
print(duck.introduce())
print(Duck.__mro__)  # 查看方法解析顺序
```

### **3.2.3 抽象基类**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

## **3.3 魔术方法**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 字符串表示
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    # 运算符重载
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # 比较运算
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # 长度
    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    # 调用对象
    def __call__(self, scale):
        return Vector(self.x * scale, self.y * scale)

# 使用示例
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)        # 加法
print(v1 == v2)       # 比较
print(len(v1))        # 长度
print(v1(2))          # 调用
```

## **3.4 设计模式示例**

### **3.4.1 单例模式**

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # 初始化代码（只在第一次创建实例时执行）
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = []

# 测试单例
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

### **3.4.2 工厂模式**

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# 使用工厂
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
```

# **第四章：文件操作与异常处理**

## **4.1 文件操作**

### **4.1.1 基本文件操作**

```python
# 打开文件的不同模式
# 'r': 只读（默认）
# 'w': 写入（会覆盖）
# 'a': 追加
# 'x': 独占写入
# 'b': 二进制模式
# 't': 文本模式（默认）
# '+': 读写模式

# 基本读取操作
with open('example.txt', 'r', encoding='utf-8') as file:
    # 读取整个文件
    content = file.read()
    
    # 读取指定字节数
    file.seek(0)  # 回到文件开头
    chunk = file.read(10)  # 读取10个字符
    
    # 读取一行
    file.seek(0)
    line = file.readline()
    
    # 读取所有行到列表
    file.seek(0)
    lines = file.readlines()
    
    # 逐行读取（内存友好）
    file.seek(0)
    for line in file:
        print(line.strip())  # strip()去除首尾空白字符

# 基本写入操作
with open('output.txt', 'w', encoding='utf-8') as file:
    # 写入字符串
    file.write('Hello, World!\n')
    
    # 写入多行
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)

# 追加模式
with open('log.txt', 'a', encoding='utf-8') as file:
    file.write('New log entry\n')
```

### **4.1.2 高级文件操作**

```python
import os
import shutil

# 文件路径操作
current_dir = os.getcwd()  # 获取当前工作目录
file_path = os.path.join('folder', 'subfolder', 'file.txt')  # 构建路径
abs_path = os.path.abspath(file_path)  # 获取绝对路径
dir_name = os.path.dirname(file_path)  # 获取目录名
base_name = os.path.basename(file_path)  # 获取文件名

# 文件操作
os.makedirs('new_folder', exist_ok=True)  # 创建目录
os.rename('old.txt', 'new.txt')  # 重命名文件
os.remove('file.txt')  # 删除文件
shutil.copy('source.txt', 'dest.txt')  # 复制文件
shutil.move('source.txt', 'new_location')  # 移动文件

# 文件信息
file_exists = os.path.exists('file.txt')  # 检查文件是否存在
is_file = os.path.isfile('file.txt')  # 是否是文件
is_dir = os.path.isdir('folder')  # 是否是目录
file_size = os.path.getsize('file.txt')  # 获取文件大小
file_stats = os.stat('file.txt')  # 获取文件详细信息

# 遍历目录
for root, dirs, files in os.walk('folder'):
    print(f'当前目录: {root}')
    print(f'子目录: {dirs}')
    print(f'文件: {files}')
```

### **4.1.3 二进制文件操作**

```python
# 读取二进制文件
with open('image.jpg', 'rb') as file:
    binary_data = file.read()

# 写入二进制文件
with open('copy.jpg', 'wb') as file:
    file.write(binary_data)

# 使用struct处理二进制数据
import struct

# 将数据打包成二进制
data = struct.pack('iif', 1, 2, 3.14)  # i:int, f:float

# 从二进制解包数据
numbers = struct.unpack('iif', data)
```

## **4.2 异常处理**

### **4.2.1 基本异常处理**

```python
# try-except 基本结构
try:
    x = int(input("请输入一个数字: "))
    result = 10 / x
except ValueError:
    print("输入必须是数字")
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:
    print(f"发生错误: {e}")
else:
    print(f"结果是: {result}")  # 只在try块成功时执行
finally:
    print("这总是会执行")  # 无论是否发生异常都会执行

# 多个异常在一起处理
try:
    # 可能引发异常的代码
    pass
except (ValueError, TypeError) as e:
    print(f"发生了值错误或类型错误: {e}")
```

### **4.2.2 自定义异常**

```python
# 定义自定义异常
class CustomError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

# 使用自定义异常
def process_age(age):
    if age < 0:
        raise CustomError("年龄不能为负数", 1001)
    if age > 150:
        raise CustomError("年龄超出正常范围", 1002)
    return age

# 处理自定义异常
try:
    age = process_age(-5)
except CustomError as e:
    print(f"错误 {e.error_code}: {str(e)}")
```

### **4.2.3 上下文管理器**

```python
# 自定义上下文管理器
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # 返回True表示异常已处理
        return False

# 使用自定义上下文管理器
with FileManager('test.txt', 'w') as file:
    file.write('Hello, World!')

# contextlib装饰器创建上下文管理器
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield  # 这里是with块中的代码执行点
    end = time.time()
    print(f"执行时间: {end - start}秒")

# 使用timer上下文管理器
with timer():
    # 执行一些耗时操作
    import time
    time.sleep(1)
```

### **4.2.4 调试和日志**

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# 创建logger
logger = logging.getLogger(__name__)

# 使用不同级别的日志
try:
    logger.debug("调试信息")
    logger.info("普通信息")
    logger.warning("警告信息")
    result = 1 / 0  # 故意制造错误
except Exception as e:
    logger.error("发生错误", exc_info=True)
    logger.critical("严重错误")

# 断言
def calculate_square_root(n):
    assert n >= 0, "输入必须是非负数"
    return n ** 0.5
```

# **第五章：高级Python特性**

## **5.1 迭代器和生成器**

### **5.1.1 迭代器**

```python
# 自定义迭代器
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# 使用迭代器
counter = CountDown(5)
for num in counter:
    print(num)  # 5, 4, 3, 2, 1

# 实现可迭代的范围类
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

# 使用自定义范围
for i in Range(1, 5):
    print(i)  # 1, 2, 3, 4
```

### **5.1.2 生成器**

```python
# 生成器函数
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用生成器
fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 前10个斐波那契数

# 生成器表达式
squares = (x**2 for x in range(10))
print(list(squares))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成器管道
def numbers():
    for i in range(1, 11):
        yield i

def squares(numbers):
    for n in numbers:
        yield n**2

def evens(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

# 使用生成器管道
pipeline = evens(squares(numbers()))
print(list(pipeline))  # [4, 16, 36, 64, 100]
```

## **5.2 装饰器进阶**

### **5.2.1 带参数的装饰器**

```python
# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")

# 类作为装饰器
class Trace:
    def __init__(self, handle_result=False):
        self.handle_result = handle_result

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            result = func(*args, **kwargs)
            if self.handle_result:
                print(f"Result: {result}")
            return result
        return wrapper

@Trace(handle_result=True)
def add(a, b):
    return a + b
```

### **5.2.2 多重装饰器**

```python
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def hello():
    return "Hello, World!"

print(hello())  # <b><i>Hello, World!</i></b>
```

## **5.3 元类和类装饰器**

### **5.3.1 元类**

```python
# 自定义元类
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# 使用元类
class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

# 验证单例
db1 = Database()
db2 = Database()
print(db1 is db2)  # True

# 属性验证元类
class ValidateMeta(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, property):
                attrs[f'_validate_{key}'] = cls.create_validator(key)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def create_validator(name):
        def validator(self, value):
            if value < 0:
                raise ValueError(f"{name} must be positive")
            return value
        return validator
```

### **5.3.2 描述符**

```python
# 描述符示例
class Positive:
    def __init__(self):
        self._value = {}
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._value.get(instance, 0)
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        self._value[instance] = value

class Point:
    x = Positive()
    y = Positive()

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

## **5.4 并发编程**

### **5.4.1 多线程**

```python
import threading
import time

# 线程安全的计数器
class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            current = self.value
            time.sleep(0.1)  # 模拟耗时操作
            self.value = current + 1

# 创建多个线程
counter = Counter()
threads = []
for _ in range(5):
    thread = threading.Thread(target=counter.increment)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"Final count: {counter.value}")

# 使用线程池
from concurrent.futures import ThreadPoolExecutor

def worker(x):
    return x * x

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(worker, range(10))
    print(list(results))
```

### **5.4.2 多进程**

```python
from multiprocessing import Process, Pool
import os

def worker(name):
    print(f'Worker {name}: {os.getpid()}')

# 创建多个进程
processes = []
for i in range(3):
    p = Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

# 等待所有进程完成
for p in processes:
    p.join()

# 使用进程池
def f(x):
    return x * x

with Pool(5) as p:
    print(p.map(f, range(10)))
```

### **5.4.3 异步编程**

```python
import asyncio

async def async_hello(name, delay):
    await asyncio.sleep(delay)
    print(f'Hello, {name}')

async def main():
    # 创建任务
    tasks = [
        async_hello("Alice", 2),
        async_hello("Bob", 1),
        async_hello("Charlie", 3)
    ]
    # 并发执行
    await asyncio.gather(*tasks)

# 运行异步程序
asyncio.run(main())

# 异步上下文管理器
class AsyncResource:
    async def __aenter__(self):
        print("获取资源")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("释放资源")

async def use_resource():
    async with AsyncResource() as res:
        print("使用资源")
```

# **第六章：常用标准库**

## **6.1 文本处理**

### **6.1.1 string 模块**

```python
import string

# 常用字符串常量
print(string.ascii_letters)   # 所有字母
print(string.digits)         # 数字
print(string.punctuation)    # 标点符号
print(string.whitespace)     # 空白字符

# 字符串模板
template = string.Template('Hello, $name! You have $amount dollars.')
result = template.substitute(name='Alice', amount=100)
print(result)
```

### **6.1.2 re 模块（正则表达式）**

```python
import re

text = "My email is user@example.com and phone is 123-456-7890"

# 匹配模式
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

# 查找所有匹配
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

# 替换
new_text = re.sub(phone_pattern, '***-***-****', text)

# 分割文本
words = re.split(r'\W+', text)

# 使用编译后的正则表达式（提高性能）
email_regex = re.compile(email_pattern)
matches = email_regex.finditer(text)
for match in matches:
    print(f"Found email at position {match.start()}: {match.group()}")
```

## **6.2 日期和时间**

### **6.2.1 datetime 模块**

```python
from datetime import datetime, date, time, timedelta
import pytz  # 处理时区

# 获取当前日期和时间
now = datetime.now()
today = date.today()

# 创建日期和时间
specific_date = date(2023, 12, 31)
specific_time = time(13, 30, 0)
specific_datetime = datetime(2023, 12, 31, 13, 30, 0)

# 日期格式化
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
parsed = datetime.strptime("2023-12-31 13:30:00", "%Y-%m-%d %H:%M:%S")

# 时间计算
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
two_hours_later = now + timedelta(hours=2)

# 处理时区
utc = pytz.UTC
pacific = pytz.timezone('US/Pacific')
utc_time = datetime.now(utc)
pacific_time = utc_time.astimezone(pacific)
```

## **6.3 数据处理**

### **6.3.1 json 模块**

```python
import json

# Python对象转JSON
data = {
    'name': 'Alice',
    'age': 30,
    'cities': ['New York', 'London'],
    'active': True,
    'height': 1.75
}

# 序列化到字符串
json_str = json.dumps(data, indent=4)
print(json_str)

# 序列化到文件
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# 从字符串解析
parsed_data = json.loads(json_str)

# 从文件解析
with open('data.json', 'r') as f:
    loaded_data = json.load(f)

# 自定义JSON编码
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_encoder(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age}
    raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

person = Person('Bob', 25)
json_str = json.dumps(person, default=person_encoder)
```

### **6.3.2 csv 模块**

```python
import csv

# 写入CSV文件
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London']
]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 使用字典写入
dict_data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'London'}
]

with open('dict_data.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict_data)

# 读取CSV文件
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 读取为字典
with open('dict_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
```

## **6.4 系统和OS操作**

### **6.4.1 os 和 sys 模块**

```python
import os
import sys
import platform

# 系统信息
print(sys.platform)          # 操作系统平台
print(sys.version)          # Python版本
print(platform.system())    # 操作系统名称
print(os.name)             # 操作系统类型

# 环境变量
print(os.environ.get('PATH'))
os.environ['MY_VAR'] = 'value'

# 路径操作
current_dir = os.getcwd()
os.chdir('..')             # 改变当前目录
path = os.path.join('folder', 'subfolder', 'file.txt')
abs_path = os.path.abspath(path)
norm_path = os.path.normpath(path)

# 目录操作
os.makedirs('new/nested/directory', exist_ok=True)
os.removedirs('new/nested/directory')
for root, dirs, files in os.walk('.'):
    print(f"当前目录: {root}")
    print(f"子目录: {dirs}")
    print(f"文件: {files}")

# 进程管理
pid = os.getpid()          # 当前进程ID
os.system('echo Hello')    # 执行系统命令
```

### **6.4.2 argparse 模块**

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='示例命令行程序')
    
    # 添加参数
    parser.add_argument('name', help='用户名')
    parser.add_argument('-a', '--age', type=int, help='年龄')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    
    # 解析参数
    args = parser.parse_args()
    
    # 使用参数
    print(f"Hello, {args.name}")
    if args.age:
        print(f"You are {args.age} years old")
    if args.verbose:
        print("Verbose mode enabled")

if __name__ == '__main__':
    main()
```

### **6.4.3 logging 模块**

```python
import logging

# 基本配置
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

# 创建logger
logger = logging.getLogger(__name__)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建文件处理器
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)

# 创建格式器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 添加处理器到logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 记录不同级别的日志
logger.debug('调试信息')
logger.info('一般信息')
logger.warning('警告信息')
logger.error('错误信息')
logger.critical('严重错误')
```

# **第七章：算法与数据结构**

## **7.1 基本数据结构实现**

### **7.1.1 链表**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# 使用示例
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
print(ll.display())  # [0, 1, 2]
ll.delete(1)
print(ll.display())  # [0, 2]
```

### **7.1.2 栈和队列**

```python
# 栈实现
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# 队列实现
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Queue is empty")
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
```

### **7.1.3 二叉树**

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    # 中序遍历
    def inorder(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements
    
    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.data)
            self._inorder_recursive(node.right, elements)
    
    # 前序遍历
    def preorder(self):
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements
    
    def _preorder_recursive(self, node, elements):
        if node:
            elements.append(node.data)
            self._preorder_recursive(node.left, elements)
            self._preorder_recursive(node.right, elements)
    
    # 后序遍历
    def postorder(self):
        elements = []
        self._postorder_recursive(self.root, elements)
        return elements
    
    def _postorder_recursive(self, node, elements):
        if node:
            self._postorder_recursive(node.left, elements)
            self._postorder_recursive(node.right, elements)
            elements.append(node.data)
```

## **7.2 排序算法**

### **7.2.1 基本排序算法**

```python
# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```

### **7.2.2 高级排序算法**

```python
# 快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 堆排序
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr
```

## **7.3 搜索算法**

```python
# 二分查找
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# 深度优先搜索 (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for next_vertex in graph[start]:
        if next_vertex not in visited:
            dfs(graph, next_vertex, visited)
    
    return visited

# 广度优先搜索 (BFS)
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited
```

# **第八章：动态规划与贪心算法**

## **8.1 动态规划基础**

### **8.1.1 基本概念与实现方法**

```python
# 斐波那契数列 - 展示不同实现方法
# 1. 递归实现（效率低）
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 2. 记忆化递归（自顶向下）
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# 3. 动态规划（自底向上）
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 4. 空间优化的动态规划
def fib_optimized(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

### **8.1.2 经典动态规划问题**

```python
# 1. 最长递增子序列 (LIS)
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n  # dp[i]表示以arr[i]结尾的LIS长度
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 2. 编辑距离
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化边界
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # 填充dp表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j],      # 删除
                              dp[i][j-1],        # 插入
                              dp[i-1][j-1]) + 1  # 替换
    
    return dp[m][n]

# 3. 背包问题
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                              dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# 4. 最长公共子序列 (LCS)
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # 重构最长公共子序列
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))
```

## **8.2 贪心算法**

### **8.2.1 基本贪心问题**

```python
# 1. 找零钱问题
def make_change(coins, amount):
    coins.sort(reverse=True)  # 从大到小排序
    result = []
    remaining = amount
    
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    
    return result if remaining == 0 else None

# 2. 活动选择问题
def activity_selection(start, finish):
    n = len(start)
    # 按结束时间排序
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]
    
    return selected

# 3. 区间调度问题
def interval_scheduling(intervals):
    # 按结束时间排序
    intervals.sort(key=lambda x: x[1])
    selected = [intervals[0]]
    last_end = intervals[0][1]
    
    for interval in intervals[1:]:
        if interval[0] >= last_end:
            selected.append(interval)
            last_end = interval[1]
    
    return selected
```

### **8.2.2 高级贪心问题**

```python
# 1. Huffman编码
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(chars, freqs):
    nodes = [HuffmanNode(c, f) for c, f in zip(chars, freqs)]
    
    while len(nodes) > 1:
        # 获取频率最小的两个节点
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        # 创建新的内部节点
        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right
        
        nodes.append(internal)
    
    return nodes[0]

def get_huffman_codes(root, code="", codes=None):
    if codes is None:
        codes = {}
    
    if root:
        if root.char:
            codes[root.char] = code
        get_huffman_codes(root.left, code + "0", codes)
        get_huffman_codes(root.right, code + "1", codes)
    
    return codes

# 2. 最小生成树 (Prim算法)
def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    edges = []
    
    for _ in range(n - 1):
        minimum = float('inf')
        x = y = 0
        
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x, y = i, j
        
        selected[y] = True
        edges.append((x, y, graph[x][y]))
    
    return edges
```

# **第九章：高级算法与技巧**

## **9.1 图论算法**

### **9.1.1 图的表示与基本操作**

```python
# 图的邻接表表示
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2, directed=False):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)
        
        self.graph[v1].append(v2)
        if not directed:
            self.graph[v2].append(v1)
    
    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                edges.append((vertex, neighbor))
        return edges
```

### **9.1.2 最短路径算法**

```python
# Dijkstra最短路径算法
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.keys())
    path = {}
    
    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])
        
        if distances[current] == float('infinity'):
            break
            
        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current
                
        unvisited.remove(current)
    
    return distances, path

# Floyd-Warshall算法
def floyd_warshall(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    dist = {i: {j: float('infinity') for j in vertices} for i in vertices}
    
    # 初始化距离矩阵
    for i in vertices:
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]
    
    # 核心算法
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
```

### **9.1.3 最小生成树算法**

```python
# Kruskal算法
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((weight, u, v))
    
    edges.sort()  # 按权重排序
    vertices = list(graph.keys())
    uf = UnionFind(vertices)
    mst = []
    
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
    
    return mst
```

## **9.2 高级数据结构**

### **9.2.1 平衡二叉树（AVL树）**

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = max(self.get_height(y.left),
                      self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left),
                      self.get_height(x.right)) + 1
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = max(self.get_height(x.left),
                      self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left),
                      self.get_height(y.right)) + 1
        
        return y
    
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root
        
        root.height = max(self.get_height(root.left),
                         self.get_height(root.right)) + 1
        
        balance = self.get_balance(root)
        
        # 左左情况
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # 右右情况
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # 左右情况
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # 右左情况
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
```

### **9.2.2 红黑树**

```python
class Color:
    RED = True
    BLACK = False

class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = Color.RED

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = Color.BLACK
        self.root = self.NIL
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def insert(self, key):
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        
        self.fix_insert(node)
    
    def fix_insert(self, k):
        while k.parent and k.parent.color == Color.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = Color.BLACK
```
