def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
result = add(num1, num2)
print(f"The sum of {num1} and {num2} is {result}.")
