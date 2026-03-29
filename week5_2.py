def fibonacci_recursive(n):
       if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series (Iteration):")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
print("Fibonacci Series (Recursion):")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
