TICKET_PRICE = 10

tickets_remaining = 100

# Run this code continuously until we run out of tickets.
while tickets_remaining >= 1:

	# Output how many tickets are remaining using the tickets_remaining variable

	print("There are currently {} tickets remaining.".format(tickets_remaining))

	# Gather the users name and assign it to a new variable
	user_name = input("What is your name?  ")

	# Prompt the user by name and ask how many tickets they woule like
	quantity = input("{}, how many tickets would you like to purchase?  ".format(user_name))
	quantity = int(quantity)
	# Calculate the price (number of tickets * price) and assign to a variable
	purchase_total =  TICKET_PRICE * quantity

	# Output the price to the screen
	print("{}, your total for {} tickets will be {}.".format(user_name, quantity, purchase_total))

	# Prompt user if they want to proceed. Y/N
	user_confirm = input("{}, would you like to proceed with this purchase of {}? Y/N  ".format(user_name, purchase_total))

	# If they want to proceed
	if user_confirm.lower() == 'y':

		# print out to the screen "SOLD!" to confirm purchase
		# TODO: Gather credit card info and process it.
		print("SOLD!! Thank you for your purchase of {}.".format(purchase_total))
		# decrement the tickets remaining by the number of tickets purchased
		tickets_remaining -= quantity

	# Else
	else: 
		print("Thanks anyways, {}!!".format(user_name))
		# Thank them by name

print("I\'m sorry, the tickets are all sold out. :(")

# Notify user that the tickets are sold out.