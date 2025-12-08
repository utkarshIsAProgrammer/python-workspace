# list

food = ["pizza", "cucumber", "tomato", "potato", "pudding"]

food[0] = "sushi"
print(food, food[::2])

food.append("tofu")
food.pop()
food.insert(1, "fish")
food.sort()
food.clear()

for item in food:
    print(item)

# 2D list
drink = ["coffee", "soda", "hotdog"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drink, dinner, dessert]  # 2d list
print(food[0][0])
