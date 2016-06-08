fib = [1, 2, 3, 5, 8, 13, 21]

# this throws no error
print(fib[3])

try:
	print("What # element do you want?")
	print(fib[int(raw_input())])
except: 
	print("Sorry, your # was too high!")

# this throws an error
# print(fib[18])
