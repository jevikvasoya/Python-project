menu = {
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad' : 70,
    'coffee': 80
    }

#greet
print("welcome to python hotel")
print(" pizza: $40\n pasta: $50\n burger: $60\n salad: $70\n coffee: $80")

order_total = 0

item_1 = input("enter order you want = ")

if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"your item {item_1} has been added")

else:
    print(f"orderd item {item_1} is not avialable yet")

another_item = input("do you want add another item (yes/no)")

if another_item == "yes":
    item_2 = input("enter second item")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added")
    
    else:
        print(f"item {item_2} is not available")

print(f"total amount to pay {order_total}")