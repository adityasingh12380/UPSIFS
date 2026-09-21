def add_entry(d):
    d["age"] = 20


def reassign_dict(d):
    d = {"name": "Aditya", "age": 25}
    print("Inside reassign function:", d)


my_dict = {"name": "Aditya"}

print("Original dictionary:", my_dict)

add_entry(my_dict)
print("After add_entry:", my_dict)

reassign_dict(my_dict)
print("After reassign_dict:", my_dict)