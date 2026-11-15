
# Assignment 1: Fibonacci Series
# Aim: To implement Fibonacci series using recursive and
# non-recursive methods and analyze their time and space complexity.

# Recursive method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Non-recursive (iterative) method
def fibonacci_iterative(n):
    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


# Main program
n = int(input("Enter the number of terms: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print("\nFibonacci series using recursive method:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print("\n\nFibonacci series using non-recursive method:")
    print(*fibonacci_iterative(n))

    print("\n\nTime and Space Complexity:")
    print("Recursive: Time O(2^n), Space O(n)")
    print("Iterative: Time O(n), Space O(n) for storing the series")
