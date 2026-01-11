"""
ของ ณัฐภัทร วรจินดา
หน้าที่: Main
"""
from input import get_user_input
from output import sort_numbers

def main():
    numbers, algorithm = get_user_input()
    result = sort_numbers(numbers, algorithm)

    if result is None:
        print("Invalid algorithm. Choose 1, 2, b, q, bubble, or quick.")
    else:
        print("Original:", numbers)
        print("Sorted result:", result)


if __name__ == "__main__":
    main()