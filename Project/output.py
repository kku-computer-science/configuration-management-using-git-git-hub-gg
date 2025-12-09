from bubble_sort import bubble_sort
from quick_sort import quick_sort
def sort_numbers(numbers, algorithm):
    arr = list(map(int, numbers.split()))
    if algorithm == "bubble":
        return bubble_sort(arr.copy())
    elif algorithm == "quick":
        return quick_sort(arr.copy())
    else:
        return None
