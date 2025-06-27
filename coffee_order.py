class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No items in your order.")
            return
        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total():.2f}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()
        confirm = input("Please confirm your order (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Thank you for your order!")
            self.items.clear()
        else:
            print("Checkout cancelled.")

def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0),
        Coffee("Mocha", 3.5)
    ]
    order = Order()

    while True:
        print("\nCoffee Menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ").strip()
        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) - 1])
        elif choice == '5':
            order.show_order()
        elif choice == '6':
            order.checkout()
        elif choice == '7':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

# This ensures the main() function runs
if __name__ == "__main__":
    main()
