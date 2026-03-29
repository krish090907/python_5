def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 (Iterative) is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} (Iterative) is {factorial}")
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print(f"Factorial of {num} (Recursive) is {factorial_recursive(num)}")

