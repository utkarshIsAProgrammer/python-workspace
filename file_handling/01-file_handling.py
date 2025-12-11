# file handling

# writing to a file
with open("./file_handling/demo.txt", "w") as file:
    file.write("Hello, Python!\n")

# reading from a file
with open("./file_handling/demo.txt", "r") as file:
    content = file.read()
    print("Content after writing:")
    print(content)

# appending to a file
with open("./file_handling/demo.txt", "a") as file:
    file.write("Appended line.\n")

# reading the file
with open("./file_handling/demo.txt", "r") as file:
    content = file.read()
    print("Content after appending:")
    print(content)
