import calendar
y = int(input("Dwste to zitoumeno etos : "))
m = 13 #in order to enter the loop 
while (m>12 or m<= 0): #check if the given number can relate to a month
	m = int(input("Dwste ton zitoumeno mina : "))
	if m>12:
		print "den yparxei autos o mhnas, dwste allo"
	

print(calendar.month(y, m))