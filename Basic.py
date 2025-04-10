class basics:

    # 一、获取多行输入组成二维数组
    n = 3  # 表示接下来有 3 行输入
    arr = [list(map(int, input().split())) for _ in range(n)]

    """
    说明：
    - input().split()：把一行字符串按空格切分成列表，例如 "1 2 3" -> ["1", "2", "3"]
    - map(int, ...)：将列表中的每个字符串转成整数
    - list(...)：将 map 返回的迭代器转为列表
    - [ ... for _ in range(n)]：执行 n 次输入，构成二维列表
    - _ 是变量名的占位符，表示“我不关心这个变量”，也可写成 i 或 line 等
    """

    # 二、获取一行输入并分别赋值给多个变量
    a, b = map(int, input().split())

    """
    说明：
    - input()：获取如 "3 5" 的输入
    - .split()：分割为 ["3", "5"]
    - map(int, ...)：转换为整数 [3, 5]
    - a, b = ...：拆包赋值给变量
    """

    # 三、map 是什么？
    """
    map 是 Python 的内置函数，用法为 map(function, iterable)
    - 会将 function 作用于 iterable 的每个元素
    - 返回一个“懒计算”的迭代器对象（map 类型）

    例如：
    nums = ["1", "2", "3"]
    mapped = map(int, nums)      # 返回 map 对象
    print(list(mapped))          # 输出 [1, 2, 3]
    """


class algorizm:
    # 冒泡排序
    def bubble(nums):
        """
        一层循环用于确定循环次数
        每次循环中，两两确认大小直至将最大的元素放在末尾
        每放一个元素到末尾，下次两两确认循环就不需要遍历到最后面已经排序号的区间
        :param nums:
        :return:
        """
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]: nums[j], nums[j + 1] = nums[j+1], nums[j]
        return nums

    # 选择排序
    def select(nums):
        """
        分两侧，一侧是排序完的，一侧没有
        先将第一个元素默认当成最小的，取其索引赋值为 min_i
        遍历当前 i 元素右侧全部元素，找有没有比这个更小的值，有则这两个交换位置
        :param nums:
        :return:
        """
        for i in range(len(nums) - 1):
            min_i = i  # 开始记录当前索引
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_i]: min_i = j  # 出现更小的值，重新把更小值的索引给到 min_i
            if i != min_i:  # 发现跟当前索引不同，说明有更小值，需要进行交换
                nums[i], nums[min_i] = nums[min_i], nums[i]  # 交换两者位置
        return nums

#