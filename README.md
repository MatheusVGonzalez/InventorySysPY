# 📦 Inventory Management System

A simple Python-based Inventory Management System that allows you to add, view, update, and remove products.  
The data can be saved into a `.txt` file when exiting the program.

---

## 🚀 Features
- ➕ **Add products** to the inventory  
- 📋 **View full inventory**  
- ✏️ **Update products** (quantity and price)  
- 🗑️ **Remove products** from the inventory  
- 💾 **Save inventory** to file on exit  

---

## 📂 Project Structure
inventory_system/
│-- inventory.txt # File where inventory data is saved
│-- main.py # Main program file
│-- README.md # This file

---

## ⚙️ How to Run
1. Clone or download the repository:  
```bash
git clone https://github.com/your-username/inventory-system.git
cd inventory-system
Run the program with Python:

bash
Copy code
python main.py
Choose an option from the menu:

1. Add Item
2. View Inventory
3. Update Item
4. Remove Item
5. Exit
🛠️ Example Usage
Welcome to the Inventory Management System!

1. Add Item 
2. View Inventory 
3. Update Item 
4. Remove Item 
5. Exit

Select an option: 1
Enter Product Name: Headset
Available categories:  ['Eletronics', 'Home', 'Office']
Enter Category (Eletronics, Home, Office): Eletronics
Enter Brand Name: Razer
Enter Quantity: 2
Enter Price: 699.99

Item added successfully!
📑 Notes
The inventory is stored in memory while the program is running.

On Exit (option 5), all data is saved into inventory.txt.

The system can be extended to use JSON, SQLite, or even a GUI in the future.