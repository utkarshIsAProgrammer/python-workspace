# countdown timer program

import time

my_time = int(input("Enter the time in seconds: "))


# normal timer
for i in range(1, my_time + 1):
    print(i)
    time.sleep(1)

print("TIME'S UP!")


# reverse timer
for i in range(my_time, 0, -1):
    print(i)
    time.sleep(1)
print("TIME'S UP!")
