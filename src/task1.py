def count_decimal_places(number: float) -> int:
    number_str = str(number)
    if '.' in number_str:
        return len(number_str.split('.')[1])
    else:
        return 0

def compare_decimal_places(num1: float, num2: float) -> str:
    count1 = count_decimal_places(num1)
    count2 = count_decimal_places(num2)
    
    if count1 > count2:
        return f"The first number ({num1}) has more decimal places ({count1}) than the second number ({num2}) ({count2})."
    elif count2 > count1:
        return f"The second number ({num2}) has more decimal places ({count2}) than the first number ({num1}) ({count1})."
    else:
        return f"Both numbers ({num1} and {num2}) have the same number of decimal places ({count1})."

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(compare_decimal_places(num1, num2))
