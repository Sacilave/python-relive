import os
import sys

n, m = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(n)]
print(lis)


# 数字字符串计数（包含3和7）
def count_valid_strings():
    """
    小蓝要构造一个长度为 10000 的数字字符串，有以下要求：

    1. 不能出现数字 0；
    2. 必须包含数字 3 和数字 7。

    求满足要求的字符串个数，结果对 10^9 + 7 取模。

    解题思路：
    - 所有可能的字符串总数为 9^10000（每位可选1~9）
    - 使用容斥原理排除不合法情况：
        - 不含3的有 8^10000 种
        - 不含7的有 8^10000 种
        - 同时不含3和7的有 7^10000 种
    - 合法数量 = 9^10000 - 2 * 8^10000 + 7^10000
    - 使用快速幂计算大指数，最后对 10^9 + 7 取模
    """
    MOD = 10 ** 9 + 7

    total = pow(9, 10000, MOD)  # 所有字符串
    no_3 = pow(8, 10000, MOD)  # 不包含3
    no_7 = pow(8, 10000, MOD)  # 不包含7
    no_3_and_7 = pow(7, 10000, MOD)  # 同时不包含3和7

    # 使用容斥原理计算合法数量
    result = (total - 2 * no_3 + no_3_and_7) % MOD

    print(result)


# 硬币兑换
def max_coin_count():
    """
    小蓝手中有 2023 种不同面值的新版硬币，
    第 i 种硬币面值为 i，数量也为 i。
    可以使用两个新版硬币兑换一个面值为 coin1 + coin2 的旧版硬币。
    问：通过任意兑换后，某个面值的硬币最多能有多少个？
    """
    # 初始化一个结果数组，result[x] 表示面值为 x 的旧硬币最多能获得多少个
    result = [0 for _ in range(4047)]  # 最大面值是 2023 + 2023 = 4046

    # 枚举所有面值的组合 i 和 j（i < j），避免重复组合
    for i in range(1, 2024):
        for j in range(i + 1, 2024):
            # 由于第 i 面值有 i 个硬币，所以可以和 j 面值的硬币兑换 i 次
            result[i + j] += i

    # 最终取兑换后任意面值中数量最多的那个
    print(max(result))


# 2023
"""
12345678 到 98765432 有多少个数完全不包含2023
def findIt(i):
  find01 = i.find('2')
  if find01 == -1: return 0

  find02 = i.find('0', find01+1)
  if find02 == -1: return 0

  find03 = i.find('2', find02+1)
  if find03 == -1: return 0

  find04 = i.find('3', find03+1)
  if find04 == -1: return 0

  return 1

count = 0
for i in range(12345678, 98765432 + 1):
  if findIt(str(i)) == 0: count += 1
print(count)
"""

# 轮转数组
def rotate(self, nums, k: int) -> None:
    """
    给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
    """
    def reverse(left: int, right: int):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    n = len(nums)
    k %= n  # 防止轮转次数超过元素数量
    reverse(0, n-1)  # 先整体翻转
    reverse(0, k-1)  # 再把前 k 个翻转
    reverse(k, n-1)  # 再反转后面几个

# 加一
def plusOne(self, digits):

    for i in range(len(digits) - 1, -1, -1):  # 倒叙遍历到 0
        if digits[i] < 9:  # 如果小于9直接加1返回
            digits[i] += 1
            return digits
        digits[i] = 0  # 否则进一位
        return [1] + [0] * len(digits)

# 寻找数组的中心下标
def pivotIndex(self, nums) -> int:
    """
    给你一个整数数组 nums ，请计算数组的 中心下标 。
    数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
    如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
    如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
    """
    suml, sumr = 0, sum(nums)
    for i in range(len(nums)):
        sumr -= nums[i]
        if sumr == suml:
            return i
        suml += nums[i]
    return -1

# !!!前后缀
def prefixSuffix(nums):
    """
    给你一个整数数组 nums，返回一个新的数组 answer，其中 answer[i] 等于 nums 中 左侧所有元素的和 与 右侧所有元素的和 之和。
    要求：不要使用额外的数组（即 O(1) 额外空间，除了 answer 本身）。时间复杂度为 O(n)。
    """
    n = len(nums)
    pre = [0] * n
    suf = [0] * n
    for i in range(1, n):
        pre[i] = pre[i - 1] + nums[i - 1]
    for i in range(n - 2, -1, -1):
        suf[i] = suf[i + 1] + nums[i + 1]
    return [p + s for p, s in zip(pre, suf)]