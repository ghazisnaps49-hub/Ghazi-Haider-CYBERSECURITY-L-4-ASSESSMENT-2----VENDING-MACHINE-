"""
Assessment 2 INTRO TO PROGRAMMING
GHAZI HAIDAR
L4, VENDING MACHINE
"""

import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(message):
    engine.say(message)
    engine.runAndWait()
                                
print("\nWelcome to smart vending machine")
print("\n======== Vending Machine Menu ========")

items = {
    "G1": {"name": "Cola", "price": 2.50, "category": "Drinks", "stock": 5},
    "G2": {"name": "Water", "price": 1.50, "category": "Drinks", "stock": 5},
    "G3": {"name": "Coffee", "price": 3.00, "category": "Drinks", "stock": 5},
    "T1": {"name": "Chocolate", "price": 2.00, "category": "Snacks", "stock": 5},
    "T2": {"name": "Croissant", "price": 4.00, "category": "Snacks", "stock": 5},
    "T3": {"name": "Biscuits", "price": 10.00, "category": "Snacks", "stock": 5}
}

def display_menu():
    print("\n--- Drinks ---")
    for code, item in items.items():
        if item["category"] == "Drinks":
            print(f"{code} / {item['name']} / AED {item['price']} / Stock: {item['stock']}")

    print("\n--- Snacks ---")
    for code, item in items.items():
        if item["category"] == "Snacks":
            print(f"{code} / {item['name']} / AED {item['price']} / Stock: {item['stock']}")

def print_receipt(item,price,paid,change):
    print ("\n-----DIGITAL RECEIPT-----")
    print(f"item Purchased:{item}")
    print(f" item price :{price:.2f}AED")
    print(f"Money Inserted:{paid:.2f}AED")
    print(f"Change :{change:.2f}AED")
    print("Thank you.visit us again!")
    print("---------")

def get_item():
    while True:
        choice = input("\nEnter the item code you want to buy (or 'X' to exit): ").upper()

        if choice == "X":
            print("\nThank you for using the vending machine.")
            return None

        if choice in items:
            if items[choice]["stock"] > 0:
                return choice
            else:
                print("Sorry, this item is out of stock")
        else:
            print("Invalid item code, please try again.")

def process_payment(price):
    total_inserted = 0.0
    print(f"\nItem price: AED {price}")

    while total_inserted < price:
        try:
            money = float(input("Insert money (AED): "))
            if money <= 0:
                print("Please insert a valid amount.")
            else:
                total_inserted += money
                print(f"Total inserted: AED {total_inserted:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    change = total_inserted - price
    return change

def dispense_item(code):
    items[code]["stock"] -= 1
    print(f"\nDispensing {items[code]['name']}... Enjoy!")

def suggest_item(selected_code):
    selected_category = items[selected_code]["category"]
    print("\nSuggested item for you:")

    if selected_category == "Drinks":
        for code, item in items.items():
            if item["category"] == "Snacks" and item["stock"] > 0:
                print(f"{item['name']} - AED {item['price']}")
                break

def another_purchase():
    while True:
        choice = input("\nWould you like to buy another item? (Y/N): ").upper()
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        else:
            print("Invalid choice. Please enter Y or N.")

def main():
    print("\nWelcome to Smart Vending Machine!")

    while True:
        display_menu()
        selected_code = get_item()

        if selected_code is None:
            break

        price = items[selected_code]["price"]
        change = process_payment(price)
        dispense_item(selected_code)

        print(f"Change returned: AED {change:.2f}")
        suggest_item(selected_code)

        if not another_purchase():
            print("\nThank you for your purchase. Have a great day!")
            break

if __name__ == "__main__":
    main()
