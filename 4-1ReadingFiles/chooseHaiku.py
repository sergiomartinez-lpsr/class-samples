# ask the reader what they want to do
print("Hi, welcome to the Haiku Reader!")
print("Choose...")
print("Press 3 for a haiky about a silly person.")
print("Press 4 for a haiku about writing haikus.")
# opens both the third and fourth haiku files
thirdHaiku = open("haiku3.txt", "r")
fourthHaiku = open("haiku4.txt", "r")
# allows the user to put in what they want 
choice = int(raw_input())
# if choice equals 3 then print third haiku
if choice == 3:
	print(thirdHaiku.read())
# otherwise, if it equals 4 then print out fourth haiku
elif choice == 4:
	print(fourthHaiku.read())
