inventory = {

}

examp = {
    "name": "headset",
    "quantity": 2,
    "price" : 699.99
}

inventory[1] = examp

def selectItem():
    print(" 1. Add Item / 2. View Inventory / 3. Update Item / 4. Remove Item / 5. Exit")
    option = input("Select an option: ")
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
    else:
        print("options from 1 to 5")

def option1():
    PName = input("Enter Product Name: ")
    Category = input("Enter Category (Eletronics, Home, Office): ")
    Brand = input("Enter Brand Name: ")
    Quant = input("Enter Quantity: ")
    Price = input("Enter Price: ")
def option2():

def option3():

def option4():

def option5():

print("Welcome to the Inventory Management System!")
selectItem()
print(inventory)