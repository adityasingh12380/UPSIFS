def change_string(s):
    s = "X" + s[1:]
    print("Inside function:", s)


my_string = "Hello"

print("Before function:", my_string)

change_string(my_string)

print("After function:", my_string)
