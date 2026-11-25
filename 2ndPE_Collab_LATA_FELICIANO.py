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
product2 = productmenu("Fries", 35)
product3 = productmenu("Soft Drink", 25)
print("------------------------------")
product1.display_product()
product2.display_product()
product3.display_product()
option = input("Please select a product by entering its name: ")
if option.lower() == "burger":
    print("You have selected Burger. Price: 50Php")
elif option.lower() == "pizza":
    print("You have selected Fries. Price: 35Php")
elif option.lower() == "pasta":
    print("You have selected Soft Drink. Price: 25Php")
input("Enter quantity: ")
option = input()
option = input("Add another product? (yes/no): ")
if option.lower() == "yes":
    option = input("Please select a product by entering its name: ")
    if option.lower() == "burger":
        print("You have selected Burger. Price: 50Php")
    elif option.lower() == "pizza":
        print("You have selected Fries. Price: 35Php")
    elif option.lower() == "pasta":
        print("You have selected Soft Drink. Price: 25Php")
    input("Enter quantity: ")
    print("Thank you for your order!")
if option.lower() == "no":
    print("Thank you for your order!")
print("------------------------")