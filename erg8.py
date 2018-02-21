import random

x= [random.randint(-30, 30) for i in range(30)] #create a list of 30 random numbers from -30 to 30

temp=0
for i in range(30):
	for j in range(30):
		for k in range(30):
			if (x[i] + x[j] + x[k] == 0 ):
				temp=temp + 1#use the variable in order to check if there is at least a single combination
				print ("To athroisma twn", x[i] , 	x[j] , x[k] ,"isoute me 0")																																																	
if temp==0: 
	print  "Den uparxei sundiasmos treiwn arithmwn pou na isoute me 0"