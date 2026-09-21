def maximum(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = maximum(a, b)

print("Greater number:", result)
