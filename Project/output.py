"""
ของ ญานวิทย์ พิชญกุลมงคล
หน้าที่: output
"""
from bubble_sort import bubble_sort
from quick_sort import quick_sort

def sort_numbers(numbers, algorithm):
    arr = list(map(int, numbers.split()))
    if algorithm in ["1", "b", "bubble"]:
        return bubble_sort(arr.copy())
    elif algorithm in ["2", "q", "quick"]:
        return quick_sort(arr.copy())
    else:
        return None
