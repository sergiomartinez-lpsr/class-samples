print("How old are you?")
age = int(input())

print("What's your GPA")
GPA = float(input())

# if GPA is over 3.0 and age over 16, accept
if GPA > 3.0 and age > 16:
	print("Congrats, you've been accepted to Columbia")
else:
	print("Sorry, guess you'll have to go to Harvard instead")
