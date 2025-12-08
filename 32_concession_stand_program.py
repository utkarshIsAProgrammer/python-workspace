# Concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "soda": 1.50,
}

cart = []
total = 0

print("--------- MENU ---------")
for item, price in menu.items():
    print(f"{item:10}: ${price:.2f}")
print("------------------------")

while True:
    order = input("Select an item (q to quit): ").lower()
    if order == "q":
        break
    elif order in menu:
        cart.append(order)
        print(f"{order} added to cart.")
    else:
        print("Sorry, we don't serve that.")

print("\n------ YOUR ORDER ------")
for item in cart:
    total += menu[item]
    print(item)

print(f"\nTotal: ${total:.2f}")
