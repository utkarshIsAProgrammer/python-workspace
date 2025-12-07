# shopping cart program

item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of your item: "))
quantity = int(input("Enter the quantity of your item: "))

total = price * quantity
print(f"Total Cart: ${total}")
