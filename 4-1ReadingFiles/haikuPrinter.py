import time
# returns ours first haiku poem as an object 
myFirstHaiku = open('haiku1.txt', 'r')
# print out our haiku poem 
print('Here is the first haiku:') 
# reads the file
print(myFirstHaiku.read())
 
print('I will give you the second haiku line by line.') 
print('How many seconds should I wait between lines?')
# asks the user how long they want to wait for the lines to print 
seconds = int(raw_input())
# returns our second haiku poem as an object 
mySecondHaiku = open('haiku2.txt', 'r')
 
lineToPrint = mySecondHaiku.readline() 
while lineToPrint != "":
# it will print line by line of the poem
    print(lineToPrint)
    lineToPrint = mySecondHaiku.readline()
# it will give each line depending on how long the user wants it to
    time.sleep(seconds)
# closes both of the files we opened
myFirstHaiku.close()
mySecondHaiku.close()

