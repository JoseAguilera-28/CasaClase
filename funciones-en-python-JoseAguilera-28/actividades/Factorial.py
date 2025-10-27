def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(0))
print(factorial(7))