"""
ของ ญานวิทย์ พิชญกุลมงคล
หน้าที่: input
"""
def get_user_input():
    numbers = input("Enter integers separated by space: ")
    print("Choose algorithm:")
    print("1 = Bubble Sort")
    print("2 = Quick Sort")
    print("b = Bubble Sort")
    print("q = Quick Sort")
    algorithm = input("Your choice: ").lower()
    return numbers, algorithm

