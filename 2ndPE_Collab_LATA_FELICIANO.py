class productmenu:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def display_product(self):
        print(f"Product Name: {self.product_name}, Price: ${self.product_price}")

print("Welcome to the Product Menu!")
print("------------------------------")
print("Here are the available products:")
product1 = productmenu("Burger", 50)
product2 = productmenu("Pizza", 100)
product3 = productmenu("Pasta", 80)
print("------------------------------")
product1.display_product()
product2.display_product()
product3.display_product()
option = input("Please select a product by entering its name: ")
if option.lower() == "burger":
    print("You have selected Burger. Price: $50")
elif option.lower() == "pizza":
    print("You have selected Pizza. Price: $100")
elif option.lower() == "pasta":
    print("You have selected Pasta. Price: $80")

def quantity():
    quantity = int(input("Please enter the quantity you want to purchase: "))
    return quantity

