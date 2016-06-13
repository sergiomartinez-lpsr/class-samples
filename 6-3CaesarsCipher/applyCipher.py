# import 
import string 
# applyCipher.py
# A pogram to encrypt/decrypt user text
# using Caeaser's Cipher
#
# Author: rc.martinez.sergio [at] leadps.org

# makes a maping of encoded alphabet to decode alphabet 
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	# call alphabet, lowercase and uppercase
	alpha = string.ascii_lowercase
	alphaUp = string.ascii_uppercase
	dict = {}
	c = 0
	for l in range(0, len(alpha)):
		dict[alpha[(l + key) % 26]] = alpha[l]
	for l in range(0, len(alpha)):
		dict[alphaUp[(l + key) % 26]] = alphaUp[l]
	dict[" "] = " "
	return dict
# gets the encrypted message from user
# argument: none
# return: encoded message
def getMessage():
	print("What message would you like to decode?")
	message = raw_input()
	return message
	
# for each letter in the message, decodes and records
# argument: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	newMessage = ""
	for m in message:
		newMessage = newMessage + dictionary[m]
	return newMessage
# outputs the decoded message to the terminal 
# arguments: decoded message
# returns: none
def printMessage(message):
	print(message)

# execution starts here

# ask user for the key
print("What key would you like to use to decode?")
key = int(raw_input())


dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)
print("Here's the decoding of your message:")
printMessage(decodedMessage)

