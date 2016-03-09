# open walking instructions and read it
walking_file = open("walking_instructions.txt" , "r")

# will read one line of the file
lineToPrint = walking_file.readline()

# create a loop
while lineToPrint != "":
	# print each line of the file and add "duh"
	print(lineToPrint + ", duh")
	lineToPrint = walking_file.readline()

# close the file or else bad stuff will happen
walking_file.close()
