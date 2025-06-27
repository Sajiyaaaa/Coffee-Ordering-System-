# Define the Coffee class to represent each coffee item
class Coffee:
    def __init__(self, name, price):
        self.name = name    # Name of the coffee (e.g., Espresso)
        self.price = price  # Price of the coffee

# Define the Order class to handle the user's coffee order
class Order:
    def __init__(self):
        self.items = []  # List to store added coffee items

    # Add a coffee item to the order
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    # Calculate the total cost of the order
    def total(self):
        return sum(item.price for item in self.items)

    # Display the current order summary
    def show_order(self):
        if not self.items:
            print("No items in your order.")
            return
        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total():.2f}\n")

    # Handle the checkout process
    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()  # Display current order
        # Ask user to confirm the order
        confirm = input("Please confirm your order (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Thank you for your order!")
            self.items.clear()  # Clear the order list after checkout
        else:
            print("Checkout cancelled.")

# Main function to run the coffee ordering system
def main():
    # Coffee menu with predefined items
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0),
        Coffee("Mocha", 3.5)
    ]

    order = Order()  # Create a new order object

    # Start the main loop for user interaction
    while True:
        print("\nCoffee Menu ---")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        # Get user choice
        choice = input("Choose an option: ").strip()

        # Handle menu selections
        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) - 1])  # Add selected coffee
        elif choice == '5':
            order.show_order()  # Show current order
        elif choice == '6':
            order.checkout()  # Proceed to checkout
        elif choice == '7':
            print("Thank you for visiting!")  # Exit the app
            break
        else:
            print("Invalid choice. Please try again.")  # Error message

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()

