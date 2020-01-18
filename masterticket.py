TICKET_PRICE = 10

tickets_remaining = 100

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
