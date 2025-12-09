"""
ของ ญานวิทย์ พิชญกุลมงคล
หน้าที่: input
"""
from output import sort_numbers
numbers = input("Enter integers separated by space: ")
algorithm = input("Choose algorithm (quick/bubble): ").lower()
result = sort_numbers(numbers, algorithm)
if result is None:
    print("Invalid algorithm.")
else:
    print("Original:", numbers)
    print(f"Sorted using {algorithm} sort:", result)
