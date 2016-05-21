# contacts.py
# Author: rc.martinez.sergio [at] leadps.org

print("Welcome to Contacts!")

# make empty dictionary to add to
contacts = {}

# variable for loop
choice = 1

# loop
while choice != 0:
	print("What would you like to do?")
	print("(1) Add a phone number.")
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(4) Remove a contact.")
	print("(5) Change the number of a contact.")
	print("(0) Exit the Contacts app.")	
	choice = int(raw_input())

	# add a name and number if choice is 1
	if choice == 1:
		print("What's the name of your contact?")
		name = raw_input()
		print("What's the number of your contact?")
		num = raw_input()
		contacts[name] = num
	# print all the contacts if choice is 2
	if choice == 2:
		print(contacts)
	
	# retrieve a certain number if choice is 3
	if choice == 3:
		print("Who's number would you like?")
		name = raw_input()
		print("OK, here's the number:")
		# calls for specific contact
		print(contacts[name])

	# delete a number if choice is 4
	if choice == 4:
		print("Who's number would you like to delete?")
		name = raw_input()
		print("OK, number has been deleted.")
		# delete it
		del contacts[name]

	# change a number if choice is 5
	if choice == 5:
		print("Who's number would you like to change?")
		name = raw_input()
		print("Please enter new number:")
		num = raw_input()
		# changes to new value
		contacts[name] = num
		print("Number has been updated.")
