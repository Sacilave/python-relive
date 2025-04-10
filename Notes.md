# 数据类型

## 类型转换

### 小数字符串转换 float 时：

    “123.45” 转换为 int 类型时，使用显式转换，需先转换为 float，再转换为 int

### 数字型转换 string 时

    使用 str() 方法进行转换，如 a = 4    str(a)

### 其他进制类型

    **二进制：** 0b 开头，如 0b0101
    需要注意的是如果使用 print()，则输出为 十进制

    **十六进制：** 0x 开头，如 0xAqC2

## 字符串操作

### 字符串切片

    `a[0:1]` 索引 0 开始，截取到 索引 1 （不包括索引1的）
    包括 -1 索引也一样，到 -1 索引（不包含 -1 索引）

### 常用方法

    **.upper()** 全大写
    **.lower()** 全小写
    **.strip()** 删除开头和结尾的指定字符，默认为space符
    **.split()** 根据制定字符将字符串切片成列表，默认 space符
    **.splitlines()** 按行分割字符串
    **.find("abc", 2)** 查找子串 abc，并从 索引 2 开始 ，如未找到返回 -1，找到返回索引
    **.replace("abc", "ddd", 2) 将全部 abc 替换为 ddd，并只替换 2 次
    **.count("abc") 计算子串abc出现次数

    # startswith() - 判断是否以指定字符串开头
    text = "Hello World"
    print(text.startswith("Hello"))    # True
    print(text.startswith(("Hi", "Hello")))  # True (可以传入元组)
    
    # endswith() - 判断是否以指定字符串结尾
    print(text.endswith("World"))      # True
    
    # isalpha() - 判断是否全是字母
    print("HelloWorld".isalpha())      # True
    print("Hello123".isalpha())        # False
    
    # isdigit() - 判断是否全是数字
    print("123".isdigit())             # True
    print("123.45".isdigit())          # False
    
    # isalnum() - 判断是否是字母或数字
    print("Hello123".isalnum())        # True
    print("Hello123!".isalnum())       # False
    
    # isspace() - 判断是否全是空白字符
    print("   ".isspace())             # True
    print(" a ".isspace())             # False

### 文章字数统计

    sum( len( line.split() ) for line in a.splitlines() )

## 列表

    列表可变
    对于列表的操作无需进行 `再赋值`

### 创建列表

    # 一个列表中可以包含不同类型数据
    list01 = [1, "aba", 1.1, True]

    # 使用range创建列表，创建一个长度为 5 的列表
    list02 = list(range(5)) 

### 列表切片

    # 索引 1 到 索引 3（不包含索引3）
    list01[1:3] 

    # 索引 1 开始
    list01[1:]

    # 步长为 3 的切片，步长为索引步长
    list01[::3]

    # 反转列表
    list01[::-1]，顺序反转

### 基础方法

    # 添加元素到末尾，添加 4 到列表末尾
    list.append(4)

    # 插入元素，在列表 索引1 处插入 5 
    list.insert(1, 5)

    # 拓展列表
    list.extend([2, 4])

    # 删除元素，删除第一个 值为 5 的元素
    list.remove(5)

    # 元素出栈，可以将其赋值给一个变量
    list.pop()

    # 排序
    list.sort()

    # 反转
    list.reverse()

    # 获取指定元素的对前面的索引，获取值为3的索引
    list.index(3)

    # 计算 指定元素 出现次数
    list.count(3)

    # 列表推导式
    squares = [x**2 for x in range(5)]              # [0, 1, 4, 9, 16]
    evens = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]

## 元组

    不可变的，创建则不能更改

### 创建元组

    # 正常创建
    point = (1, 2)

    # 单元素创建时也需要逗号
    point = (1, )

    # 从列表创建
    point = tuple([1, 3, 4])

### 元组解包

    point = (3, 4)

    # x = 3, y = 4
    x, y = point  

    # a = 1, list01 = [2, 3, 4], b = 5
    a, *list01, b = (1, 2, 3, 4, 5)

### 元组操作

    # 连接元组
    point = (1, 2) + (3, 4)  # (1, 2, 3, 4)

    # 重复元组
    point = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

    # 成员检测
    ifExist = 3 in (1, 2, 3)  # True

    # 另外也可以使用 count 和 index 函数

## 集合

    无序，不重复元素，支持数学运算

### 创建集合

    collections = {1, 2, 3, 4}

    # 使用 set() 创建会直接去除重复元素
    set_collections = set([1, 2, 2, 3, 4])

### 集合操作

    print(a | b)  # 并集
    print(a & b)  # 交集
    print(a - b)  # 差集

### 集合方法

    a.add(5)  # 添加单个元素
    a.update([99, 1, 0])  # 添加多个元素
    a.remove(2)  # 删除元素，不存在会报错
    a.discard(2)  # 删除元素，不存在不会报错
    a.clear()  # 清空集合

## 字典

### 创建字典

    # 正常创建
    可以看出，字典中的值可以指向一个方法
    person = {
    "name" : "Bob",
    "age" : 11,
    "kill" : kill()
    }
    另外，还可以设置值为类的实例中的成员

    # 使用 pair 创建
    person = dict([("name", "Bob"), ("age", 11)])

### 访问
    
    # 直接访问
    person[ key ]  

    # 安全访问，如果键不存在返回 0，如果没有参数 0，则默认返回 None
    person.get( key, 0 )  

#### 获取全部 ?

    # 键
    person.keys()  
    

    # 值
    person.values()  

    # 键值对
    person.items()  
    # 遍历解包使用
    for key, value in person.items():
        print("Key: ", key)
        print("Value: ", value)
    # 转换解包使用
    person_list = list(person.items())
    person_list[1][1]  # 即为第2个键值对的值
    
    
### 修改
    
    # 修改值
    person[ key ] = value  
    
    # 添加值
    person[ newKey ] = newValue  

    # 添加多个键值对
    person.update({"food": "Ice Cream"})

    # 弹出键值对，返回指定键的值
    popped = person.pop("age")

    # 清空字典
    person.clear()
    
# 控制结构

## 条件判断 

### 普通 if 判断

### 三元条件表达式（多条件模式）

    message = "中了" if num == rand else "小了" if num < rand else "大了"
    
### 复合条件
    
    if ... and ...:

### 成员判断

    if "a" in [a, n, g]

### 身份判断

    if x is None:

### 真值判断

    if not person:
        print("person 字典为空")

    # 以下值在条件判断中都被视为False：
    **False, None, 0, 0.0, '', [], {}, set()**

## for 循环

### 基本 for 循环

    for i in range(次数)

### 普通遍历

    for item in list:

### 使用 enumerate 遍历索引和值

    for index, value in enumerate(list):

    # 如果是 字典类型，则也返回索引和键

### 字典遍历
    
    dic = {"a": 1, "b": 2 }
    for index, value in dic.items():
        print(index, value)

    # 当然也有用传统方法
    for key in dic:
        print(key, dic[key])

### 列表推导式中的 for

    numlist = [1, 2, 3, 4, 5]
    print([x**2 for x in numlist])  # 直接将整个列表进行了平方并输出

### zip 进行多列表遍历

    for alpha, num in zip(alphalist, numlist):
        print(f"{alpha}, {num}")
    
## While 循环

### 带 else 的 While循环

    # 当 while循环没有进行 break，正常结束时，运行 else 内中内容，否则不会运行
    while count >= 0:
        print(count)
        count -= 1
    else:
        print("没有break")

    # 值得一提的是 else 在循环中就是此作用

### 循环控制

    # break 退出
    # continue 继续
    # pass 什么都不做

# 异常处理

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

# 函数

## 函数定义

    def hello(name):
        print(f"hello {name}")

## 函数调用

    hello("bob")

## 函数多返回值

    # 返回，通过逗号隔开，本质上返回的是元组
    def hello(name):
        return name, name.lower() == "bob"
    
    # 获取多个返回，对元组解包
    name, isBob = hello("Bob")

## 函数参数列表

    # 普通参数列表
    def test(a, b = 1):
        return a, b
    print(test(1, 2))

    # 关键词参数(调用时)
    test(a = 1, b = 2)

    # 可变位置参数(类似于传递一个 **列表** )
    def test(*args):
        return sum(args)
    print(test(1, 2, 3))

    # 可变关键字参数（类似于传递一个 **字典** ）
    def test(**dic):
        for key, value in dic.items():
            print(key, value)

    # 另外参数可以混合使用

## 作用域

    基本一致，直接跳过
    
    global 可以将局部变量变全局变量

# 面向对象

## 基本定义

    class Dog:
        species = "Dog"  # 类变量，所有实例共享
        """
        对于 self 的解释：
        相当于调用方法时自动传入的实例对象本身
        """
        
        def __init__(self, name, age):
            self.name = name  # 将实例对象的 name 设为实例化时传入的 name参数
            self.age = age
    
        def eat(self):
            print(f"{self.name} is eating")  # 输出实例化后对象的 name 值
    
        def ageStatus(self):
            print("年幼" if self.age < 1 else "年轻" if self.age < 5 else "老年")
    
## 装饰器

### @staticmethod 静态方法装饰器

    # python 中没有 static 关键字，静态方法通过装饰器实现

    # @staticmethod

    class Calculator:
        @staticmethod
        def add(a, b):

### @classmethod 类方法装饰器

    # 类方法无需实例化对象直接调用方法

    @classmethod
    def speciesChange(cls, species):  # 传入的 cls为类本体，在调用时自动传入
        cls.species = species

### @property 属性方法

    # 将方法转换为属性，提供直接访问和计算
    # 可以通过 setter 进行修改赋值

    @property
    def theAge(self):
        return self.age

    @theAge.setter
    def theAge(self, age):
        self.age = age

    # dog1 为此类的实例对象
    print(dog1.theAge)  # 通过属性方式，而不是方法调用
    dog1.theAge = 14  # 因为设置了 setter，所以可以进行修改此属性化后的方法

## 多态与继承

### 基本继承

    # 基类
    class Animal:
    # 继承类
    class Cat(Animal):
    
    # 调用父类成员
    super().functions()

    # 重写方法只需要直接在新方法中同名重写

    # 如要求某方法必须重写，raise 异常
    raise NotImplementedError

### 多重继承

    class Cat(Animal, Cuttie, Pet):

## 魔术方法

    

    
