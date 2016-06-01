# CS 6.5 Tools for Ciphers - Indpendent Practice
# Implement the functions below - when you've finished, all tests should pass
# Author: rc.martinez.sergio [at] leadps.org


# import statements here
import string


# calls function to create a list with the letters from a to z
# DOES NOT manually create the list
# use Google and/or Stack Overflow to find how to do this in python!
# returns a list with the lowercase letters a to z
def getLowercaseAlphabet():
	lowcase_alpha = list(string.ascii_lowercase)
	return lowcase_alpha

def getUppercaseAlphabet():
	upcase_alpha = list(string.ascii_uppercase)
   	return upcase_alpha

def getReorderedLowercaseAlphabet(key):
	lowerAlpha = getLowercaseAlphabet()
	orderedAlpha = []
	c = 0
	while c < 26:
		orderedAlpha.append(lowerAlpha[(key + c) % 26])
		c = c + 1
	return orderedAlpha





# DO NOT EDIT THE TESTS BELOW HERE!
# ------------
#

low_alpha = getLowercaseAlphabet()

try:

    if(low_alpha[5] == 'f' and low_alpha[9] == 'j'):
        print("Test 1 passes! getLowercaseAlphabet() is correct.")
    else:
        print("Test 1 fails. getLowercaseAlphabet() needs more work.")
except:
    print("Test 1 fails. getLowercaseAlphabet() needs more work.")



high_alpha = getUppercaseAlphabet()

try:
    if(high_alpha[7] == 'H' and high_alpha[11] == 'L'):
        print("Test 2 passes! getUppercaseAlphabet() is correct.")
    else:
        print("Test 2 fails. getUppercaseAlphabet() needs more work.")
except:
    print("Test 2 fails. getUppercaseAlphabet() needs more work.")




reorderAlphabet = getReorderedLowercaseAlphabet(5)

try:
    if(reorderAlphabet[5]) == 'k':
        print("Test 3 passes! getReorderedLowercaseAlphabet() is correct.")
    else:
        print("Test 3 fails. getReorderedLowercaseAlphabet() needs more work.")
except: 
    print("Test 3 fails. getReorderedLowercaseAlphabet() needs more work.")

