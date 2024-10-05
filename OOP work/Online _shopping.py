class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        """Displays product details."""
        print(f"Product: {self.product_name}, Price: {self.price}, Quantity in stock: {self.quantity_in_stock}")


class ShoppingCart:
    # Class variable
    total_carts = 0

    def __init__(self):
        # Instance variable
        self.items = []
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        """Adds a product to the cart if the quantity is available."""
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Not enough stock for {product.product_name}.")

    def remove_from_cart(self, product):
        """Removes a product from the cart."""
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"Removed {item[1]} of {product.product_name} from the cart.")
                return
        print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
        """Displays all items in the cart."""
        if not self.items:
            print("The cart is empty.")
        else:
            for product, quantity in self.items:
                print(f"{product.product_name}: {quantity}")

    def calculate_total(self):
        """Calculates and returns the total price of items in the cart."""
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Creating Product objects
product1 = Product("Laptop", 1000, 5)
product2 = Product("Smartphone", 500, 10)
product3 = Product("Headphones", 100, 20)

# Displaying product information
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

# Creating ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Performing operations on cart1
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)
cart1.display_cart()
print(f"Total price in cart1: {cart1.calculate_total()}")

# Performing operations on cart2
cart2.add_to_cart(product3, 5)
cart2.remove_from_cart(product3)
cart2.display_cart()
print(f"Total price in cart2: {cart2.calculate_total()}")
