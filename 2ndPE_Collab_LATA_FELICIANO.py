class productmenu:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def display_product(self):
        print(f"Product Name: {self.product_name}, Price: ₱{self.product_price}")


class receipt:
    def __init__(self):
        self.items = []

    def add_item(self, product_name, product_price, quantity):
        self.items.append((product_name, product_price, quantity))

    def display_receipt(self):
        print("\n------------------------")
        print("           RECEIPT")
        print("------------------------")

        grand_total = 0
        for product_name, product_price, quantity in self.items:
            total_price = product_price * quantity
            grand_total += total_price
            print(f"{product_name} x{quantity}")
            print(f"  ₱{product_price} each  =  ₱{total_price}")

        print("------------------------")
        print(f"Grand Total: ₱{grand_total}")
        print("------------------------")


print("Welcome to the Product Menu!")
print("------------------------------")
print("Here are the available products:")

products = {
    "burger": productmenu("Burger", 50),
    "fries": productmenu("Fries", 35),
    "soft drink": productmenu("Soft Drink", 25)
}

for product in products.values():
    product.display_product()

print("------------------------------")

customer_receipt = receipt()

while True:
    choice = input("Please select a product: ").strip().lower()

    if choice not in products:
        print("Invalid product. Please choose Burger, Fries, or Soft Drink.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    selected_product = products[choice]
    customer_receipt.add_item(
        selected_product.product_name,
        selected_product.product_price,
        quantity
    )

    print(f"You have selected {selected_product.product_name} x{quantity}.")

    add_another = input("Add another product? (yes/no): ").strip().lower()
    if add_another == "no":
        break
    if add_another != "yes":
        print("Please answer yes or no. Ending your order.")
        break

customer_receipt.display_receipt()
print("Thank you for your order!")


