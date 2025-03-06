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

