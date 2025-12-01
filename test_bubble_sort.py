"""
冒泡排序测试 (Bubble Sort Tests)
"""

import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """测试冒泡排序功能"""
    
    def test_unsorted_array(self):
        """测试无序数组"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_sorted_array(self):
        """测试已排序数组"""
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_reverse_sorted_array(self):
        """测试逆序数组"""
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_empty_array(self):
        """测试空数组"""
        arr = []
        expected = []
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_single_element(self):
        """测试单个元素"""
        arr = [1]
        expected = [1]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_duplicate_elements(self):
        """测试重复元素"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_negative_numbers(self):
        """测试负数"""
        arr = [-5, 2, -3, 0, 8, -1]
        expected = [-5, -3, -1, 0, 2, 8]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_original_array_unchanged(self):
        """测试原数组不被修改"""
        arr = [3, 1, 4, 1, 5]
        original = arr.copy()
        bubble_sort(arr)
        self.assertEqual(arr, original)


if __name__ == "__main__":
    unittest.main()
