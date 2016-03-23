# primeLister.py

# takes myNum, an integer
# returns True if myNum is prime
# returns False if myNum is composite
def primeOrNah(myNum):
	for num in range(2,myNum):
		# if remainder is 0 then return false
		if myNum % num == 0:
			return False			
	# if it doesnt equal 0, then return true
	return True

# create an empty list to add to it 
empty_list = []
# check if every number betwen 2 and 10000 is prime or not
for number in range(2,10000):
	# make it a variable
	z = primeOrNah(number)
	# if the number is prime then add it to the list
	if z == True:
		empty_list.append(number)
# open a file and write to it
my_file = open("primeNums.txt", "w")
# write empty_list to it
my_file.write(str(empty_list))
# close the file
my_file.close()
# print out the prime numbers
print("Here's some prime numbers for you guys:")
print(empty_list)
