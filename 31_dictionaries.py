# dictionary

student = {"name": "Alice", "age": 21, "courses": ["Math", "Physics"]}
print(student["name"])

# adding a new key-value pair
student["grade"] = "A"
print(student)

# dict() constructor
student2 = dict(name="Bob", age=22, grade="B")
print(student2)


my_dict = {"name": "Alice", "age": 21, "city": "Delhi"}

# removes all items
print("Original dictionary:", my_dict)
my_dict.clear()
print("After clear():", my_dict)

# creates a shallow copy
my_dict = {"name": "Alice", "age": 21}
shallow_copy = my_dict.copy()
print("Shallow copy:", shallow_copy)

# creates a new dictionary from keys
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "unknown")
print("Fromkeys result:", new_dict)

# returns value for a key
print("Value for 'name':", my_dict.get("name"))

# returns key-value pairs
print("Items:", list(my_dict.items()))

# returns all keys
print("Keys:", list(my_dict.keys()))

# removes a key and returns its value
popped_value = my_dict.pop("age")
print("Popped value:", popped_value)
print("After pop():", my_dict)

# removes last inserted item
my_dict = {"name": "Alice", "age": 21}
last_item = my_dict.popitem()
print("Popped item:", last_item)
print("After popitem():", my_dict)

# adds or updates key-value pairs
my_dict.update({"age": 22, "city": "Mumbai"})
print("After update():", my_dict)

# returns all values
print("Values:", list(my_dict.values()))
