#Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.

            #code    price   
            # 1:     4.00,
            # 2:     4.50,
            # 3:     5.00,
            # 4:     2.00,
            # 5:     1.50 
            
#Input:
#The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

#Output:
#The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.

class Product:
    def __init__(self, code, quantity):
        self.code = code
        self.quantity = quantity
        self.price_list = {
            1: 4.00,
            2: 4.50,
            3: 5.00,
            4: 2.00,
            5: 1.50 
        }
    
    def calculate_total(self):
        # Get the price based on the code
        price_per_item = self.price_list.get(self.code, 0)
        total_price = price_per_item * self.quantity
        return total_price

# Taking input
X, Y = map(int, input().split())  # Input for product code and quantity

# Create an instance of Product class
product = Product(X, Y)

# Calculate and display the total price with 2 decimal places
print(f"Total: R$ {product.calculate_total():.2f}")
