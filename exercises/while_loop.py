"""
练习: while循环

描述：
在数字列表中查找第一个偶数。

请补全下面的函数，使用while循环在数字列表中查找并返回第一个偶数。
如果列表中没有偶数，则返回None。
"""

def find_first_even(numbers):
    """
    在数字列表中查找第一个偶数
    
    参数:
    - numbers: 整数列表
    
    返回:
    - 列表中的第一个偶数，如果没有偶数则返回None
    """
    # 请在下方编写代码
    idx = 0
    while idx < len(numbers):
        num = numbers[idx]
        if num & 1 != 1:
            return num
        idx += 1
    return None