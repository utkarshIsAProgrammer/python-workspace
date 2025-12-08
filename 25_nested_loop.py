# nested loop

# 5x5 multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()  # new line after each row
