import sqlite3
from db_bill_handler import init_db, save_order_to_db 


menu = {
    "Cheese Pizza": 80,
    "Veg Burger": 70,
    "Tea": 30,
    "Coffee": 40,
    "Dry Manchurian": 90,
    "Masala Dosa": 60,
    "Plain Dosa": 50,
    "White Pasta": 100,
    "Red Pasta": 120,
    "French Fries": 60,
    "Fanta": 20,
    "Cola": 25,
    "Soda": 30,
    "Thums Up": 35,
    "Idli Sambhar": 60,
}

cart = []
customer_name = ""


def show_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nCurrent Cart:")
    for idx, (item, quantity, price, total) in enumerate(cart, start=1):
        print(f"{idx}. {item} x {quantity} = Rs. {total}")



#----------Add Items ----------------
def add_items():
    while True:
        print("\n---- MENU ----")
        for item, price in menu.items():
            print(f"{item:15} - Rs. {price}")
        print("\nOptions: type 'done' to finish, 'r' to remove item, 'u' to update quantity")

        choice = input("Enter ITEM: ").strip()

        if choice.lower() == 'done':
            break
        elif choice.lower() == 'r':
            show_cart()
            to_remove = input("Enter item name to remove: ").strip()
            found = False
            for entry in cart:
                if entry[0].lower() == to_remove.lower():
                    cart.remove(entry)
                    print(f"Removed {to_remove} from cart.")
                    found = True
                    break
            else:
                print("Item not found in cart.")
            continue
        elif choice.lower() == 'u':
            show_cart()
            to_update = input("Enter item name to update quantity: ").strip()
            found = False
            for i, entry in enumerate(cart):
                if entry[0].lower() == to_update.lower():
                    try:
                        new_qty = int(input("Enter new quantity: "))
                        if new_qty <= 0:
                            print("Quantity should be greater than 0.")
                            continue
                        price = entry[2]
                        total = price * new_qty
                        cart[i] = (entry[0], new_qty, price, total)
                        print(f"Updated {to_update} to quantity {new_qty}.")
                        found = True

                    except ValueError:
                        print("Invalid quantity.")
                    break
            else:
                print("Item not found.")
            continue

        if choice not in menu:
            print("Item not in menu.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity should be greater than 0.")
                continue
        except ValueError:
            print("Invalid quantity.")
            continue

        price = menu[choice]
        total = price * quantity
        cart.append((choice, quantity, price, total))
        print(f"Added {choice} x {quantity} = Rs. {total}")


#------------- Print Bill --------------
from datetime import datetime


def print_bill():
    global customer_name , total
    if not cart:
        print("Cart is Empty .Nothing to bill.")
        return
    
    customer_name = input("Enter Customer Name : ").strip()
    now = datetime.now()
    time_str = now.strftime("%d-%m-%Y %I:%M:%p")

    print("\n" + "="*35)
    print(f"Bill for {customer_name}")
    print(f"Date & Time : {time_str}")
    print("="*35 + "\n")

    subtotal = 0
    print(f"{'S.No':<15}{'item':<15}{'quantity':<15}{'total':>8}")
    print("-"*35)

    for id , (item , quantity , price , total) in enumerate(cart , start=1):
        print(f"{id:<15}{item:<15}{quantity:<15}{total:>8}")
        subtotal += total

    gst = subtotal * 0.18
    total = subtotal + gst
    print(f"-"*20)
    print(f"Subtotal : {subtotal:.2f}")
    print(f"GST (18%) : {gst:.2f}")
    print(f"Total : {total:.2f}")
    print("="*35 + "\n")

    return customer_name , total



#---------- Handle Payment ---------

def handlePayment(total):
    print("-----PAYMENT-----")
    print(f"Total Amount:{total:.2f}")
    print("Payment Methods : 1. Cash 2. UPI 3. Card")
    choice = input("Select Payment Method (1/2/3) : ").strip()

    if choice == "1":
        print("Payment Recieved in Cash")
        return "Cash Recieved"
    elif choice == "2":
        upi = input("Enter UPI ID : ").strip()
        print(f"Payment Request sent to {upi}")
        return "UPI Payment Recieved"
    elif choice == "3":
        print("Card Payment Processed")
        return "Card Payment Recieved"
    else:
        print("Invalid Method")
        return "Cash"

print("Payment Done Successfully")

# -------------Function Call --------------------
if __name__ == "__main__":
    init_db()
    add_items()
    show_cart()
    final_customer_name , total = print_bill()

    if final_customer_name and cart:
        payment_method = handlePayment(total)
        save_order_to_db(final_customer_name,cart,payment_method)
        print("Thank You. Have a Great Day")