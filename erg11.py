import string
import random

#read the text file and store each line in a String list
f = open("am.txt", "r")
dictionary = f.read().split('\n')
dictionary.pop(0)
print(dictionary)


#Make 2d array of uppercase letters 100 * 100
square = [[random.choice(string.ascii_uppercase) for i in range(100)] for j in range(100)]
for row in square:
    print(row)

#search for each individual word in dictionary
#we split it to list of chars and see
#if it matches a sub-String from our list

for word in dictionary: #for each word in our dictionary
    letters = list(word) #we get the word into a characters list

    mark = [0, letters.__len__()-1] #we get its length -1 to see how many letters we have correct
    for row in square:
        for letter in row: #we get letters of each row 1 by 1
            if (letter == letters[mark[0]]): #if it is eaqual we have scored +1, if it isn't our score drops to 0
                mark[0] += 1
                if(mark[0] > mark[1]): #if it is equal then from 0, mark[0] has gone up to mark[1] + 1 = lenth of the word so every letter in our word has been identified
                    print('Found word:', word)
                    mark[0] = 0
            else:
                mark[0]=0
        mark[0]=0 #if our line ends before each letter in our word is identified then our score has to go back to 0 because we are out of letters for that row

    #everything but reversed for vertical identification of words
    for i in range(len(square)):
        for j in range(len(square[0])):
            if (square[j][i] == letters[mark[0]]):
                mark[0] += 1
                if(mark[0] > mark[1]):
                    print('Found word:', word)
                    mark[0] = 0
            else:
                mark[0]=0
        mark[0]=0