class ItemToPurchase:
	# Initialize the item with default values
	def __init__(self):
		self.item_name = "none"
		self.item_price = 0.0
		self.item_quantity = 0
        
	# calculate and print the cost of the item by multiplying quantity and price	
	def print_item_cost(self):
		# "item_name item_quantity @ item_price = item_quantity * item_price"
		print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}")

# Main section of the code
def main():
	# Function to validate numerical input for price
	def validate_price(prompt):
		while True:
			try:
				value = float(input(prompt))
				if value < 0:
					raise ValueError("Negative value is not allowed.")
				return value
			except ValueError as e:
				print(e)

	# Function to validate integer input for quantity
	def validate_quantity(prompt):
		while True:
			try:
				value = int(input(prompt))
				if value < 0:
					raise ValueError("Negative value is not allowed.")
				return value
			except ValueError as e:
				print(e)

	# Get details from user for item 1
	print("Item 1")
	item1 = ItemToPurchase()
	item1.item_name = input("Enter the item name:\n")
	item1.item_price = validate_price("Enter the item price:\n")
	item1.item_quantity = validate_quantity("Enter the item quantity:\n")
	    
	# Get details from user for item 2
	print("\nItem 2")
	item2 = ItemToPurchase()
	item2.item_name = input("Enter the item name:\n")
	item2.item_price = validate_price("Enter the item price:\n")
	item2.item_quantity = validate_quantity("Enter the item quantity:\n")	

	# Output individual item costs
	print("\nTOTAL COST")
	item1.print_item_cost()
	item2.print_item_cost()
	
	# Calculate total cost
	total_cost = (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)
	
	# Output total cost
	print(f"Total: ${total_cost:.2f}")

# Execute the main function
if __name__ == "__main__":
	main()