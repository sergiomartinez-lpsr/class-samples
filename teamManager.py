# makes our class
class Player(object):
	# let's make our first object
        def __init__(self, name, age, goals):
		self.name  = name
		self.age = age
		self.goals = goals
	# makes function to print out the stats
	def printStats(self):
		print("Name:" + self.name)
		print("Age:" + self.age)
		print("Goals:"+ self.goals)
# makes an empty list in order to add players to it
myPlayers = []
# asks user what they want to do
print("Hello, welcome to the new Richmond's soccer team.")
print("Too add players press 1. To see the list of players press 2.")
# allows user to choose their option
choice = raw_input()
# creates a while loop to give the user different choices on what they want to do
while choice != "0":
	if choice == "1":
		# if their choice is 1 then ask them for the stats
		print("Alright, you want to add a player.")
		print("Enter name:")
		# allows user to enter their stats
		name = raw_input()
		print("Enter age:")
		age = (raw_input())
		print("Enter goals:")
		goals =(raw_input())
		# adds the player to the list
		myPlayers.append(Player(name, age, goals))
		print("Player was succesfully added.")	
	elif choice == "2":
		# prints out stats of players if the user's choice is 2
		print("Alright you want to see the stats.")
		for player in myPlayers:
			# prints stats
			player.printStats()
	# ask the user what they want to do one more time
	print("Now, do you want to add another player, press 1 or do you want to see the stats, press 2?") 
	# if the user wants to exit the program then they should press 0
	print("Or press 0 to get out.")
	# allows the user to input their choice
	choice = raw_input()
