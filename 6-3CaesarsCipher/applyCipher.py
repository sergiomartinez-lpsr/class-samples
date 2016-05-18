# applyCipher.py
# A pogram to encrypt/decrypt user text
# using Caeaser's Cipher
#
# Author: rc.martinez.sergio [at] leadps.org

# makes a maping of encoded alphabet to decode alphabet 
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):

	# placeholder
	return {}
# gets the encrypted message from user
# argument: none
# return: encoded message
def getMessage():
	pass

# for each letter in the message, decodes and records
# argument: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	pass

# outputs the decoded message to the terminal 
# arguments: decoded message
# returns: none
def printMessage(message):
	pass

# execution starts here

# ask user for the key
print("What key would you like to use to decode?")

key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)

printMessage(decodedMessage)
