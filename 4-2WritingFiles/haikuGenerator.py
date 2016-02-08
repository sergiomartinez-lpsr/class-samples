print("Welcome to the Haiku generator!")
# asks the reader for their first line of haiku 
print("Provide the first line of your haiku:") 
# allows them to input their haiku
line1 = raw_input()
# asks for the second line of haiku
print("Provide the second line of your haiku:") 
line2 = raw_input()
# asks for the third line of their haiku
print("Provide the third line of your haiku:")
line3 = raw_input()
# asks for what the user wants to name their file
print("What file would you like to write your haiku to?")
user_file = raw_input()
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")

# makes and allows to open the file and write in it
their_file = open(user_file, "w")
# adds line 1
# \n allows them to print their haiku in seperate lines
their_file.write(line1 + "\n")
# adds second line
their_file.write(line2 + "\n")
# adds third line al
their_file.write(line3 + "\n")
# closes the file
their_file.close()
