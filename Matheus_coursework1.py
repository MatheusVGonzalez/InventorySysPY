inventory = {
}
categories = ["Eletronics", "Home", "Office"]
pIds = set() 
examp = {
    "name": "headset",
    "category": "Eletronics",
    "brand": ("Razer",),
    "quantity": 2,
    "price" : 699.99
}

inventory[1] = examp
pIds.add(1)

class Product:
    def __init__(self, name, category, brand, quantity, price):
        self.name = name
        self.category = category
        self.brand = brand
        self.quantity = quantity
        self.price = price

    def u_quatity(self, Nquantity):
        self.quantity = Nquantity
    def u_price(self, Nprice):
        self.price = Nprice
    def detail(self):
        print(f"Name: {self.name} / Brand: {self.brand} / Category: {self.category} / Price: {self.price} / Quantity: {self.quantity}")
class PerishableProduct(Product):
    def __init__(self, name, category, brand, quantity, price, expdate):
        super().__init__(name, category, brand, quantity, price)
        self.expdate = expdate
    
    def display(self):
        print(super().detail() + f" / Expiration Date: {self.expdate}")

def selectItem():
    while True:
        print(" \n1. Add Item \n2. View Inventory \n3. Update Item \n4. Remove Item \n5. Exit\n")
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Number between 1 and 5")
            continue
        if(option == 1):
            option1()
        elif(option == 2):
            option2()
        elif(option == 3):
            option3()
        elif(option == 4):
            option4()
        elif(option == 5):
            option5()
            break
        else:
            print("options from 1 to 5")

def option1():
    PName = input("Enter Product Name: ")
    print("Available categories: ", categories)
    Category = input("Enter Category (Eletronics, Home, Office): ")
    Brand = input("Enter Brand Name: ")
    Brand = (Brand,)
    Quant = int(input("Enter Quantity: "))
    Price = float(input("Enter Price: "))
    
    newdict = {
        "name": PName,
        "category": Category,
        "brand": Brand,
        "quantity": Quant,
        "price": Price
    }

    newid = max(inventory.keys()) + 1
    inventory[newid] = newdict
    print("\nItem added sucessfully!")

def option2():
    print("\nCurrent Inventory:")
    for newid, item in inventory.items():
        print(f"ID: {newid} | Name: {item['name']} | Brand: {item.get('brand', '-')}")
        print(f"Category: {item.get('category', '-')} | Price: ${item['price']} | Quantity: {item['quantity']}")

def option3():
    pid = int(input("Enter productID: "))
    if pid not in inventory:
        print("Product not found")
        return

    print("1. Update Quantity\n2. Update Price")
    updOption = int(input("Select what to update: "))

    if updOption == 1:
        new_q = int(input("Enter new quantity: "))
        inventory[pid]["quantity"] = new_q
        print("Quantity updated successfully!")
    elif updOption == 2:
        new_p = float(input("Enter new price: "))
        inventory[pid]["price"] = new_p
        print("Price updated successfully!")
    else:
        print("Invalid")

def option4():
    pid = int(input("Enter productID: "))
    if pid in inventory:
        del inventory[pid]
        pIds.discard(pid)
        print("Item removed successfully!")
    else:
        print("Product not found")

def option5():
    with open("inventory.txt", "w") as f:
        for pid, item in inventory.items():
            f.write(f"ID: {pid} / {item}\n")
    print("Exiting")
    return True
    

print("Welcome to the Inventory Management System!")
selectItem()

