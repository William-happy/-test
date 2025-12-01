"""
冒泡排序实现 (Bubble Sort Implementation)

冒泡排序是一种简单的排序算法，它重复地遍历要排序的列表，
比较相邻的元素，如果顺序错误就交换它们。
"""


def bubble_sort(arr):
    """
    使用冒泡排序对数组进行排序
    
    参数:
        arr: 需要排序的列表
    
    返回:
        排序后的列表
    
    时间复杂度: O(n^2)
    空间复杂度: O(n) - 创建了输入数组的副本
    """
    # 创建数组的副本，避免修改原数组
    arr = arr.copy()
    n = len(arr)
    
    # 外层循环控制遍历次数
    for i in range(n):
        # 标记是否发生交换，用于优化
        swapped = False
        
        # 内层循环进行相邻元素比较
        # 每次循环后，最大的元素会"冒泡"到末尾
        for j in range(0, n - i - 1):
            # 如果前面的元素大于后面的元素，交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def main():
    """
    演示冒泡排序的使用
    """
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [],  # 空数组
        [1],  # 单个元素
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"  原数组: {arr}")
        sorted_arr = bubble_sort(arr)
        print(f"  排序后: {sorted_arr}")
        print()


if __name__ == "__main__":
    main()
