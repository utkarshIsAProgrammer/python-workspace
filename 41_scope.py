# local scope


def my_function():
    local_var = "I'm local"
    print(local_var)


my_function()
# print(local_var)  # this would raise a NameError


# global scope
global_var = "I'm global"


def new_function():
    print(global_var)


new_function()
print(global_var)


# global keyword
count = 0


def increment():
    global count
    count += 1
    print("Inside function:", count)


increment()
print("Outside function:", count)
