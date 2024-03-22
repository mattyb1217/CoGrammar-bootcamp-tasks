# a program to ask the user to enter a number
# state a range the numbers can be in
# use int(input(""))
#when "-1" is picked state the loop has ended and no more questions will be asked

total_number= 0
amount_inputted= 0

number= int(input("Say a number between -5 and 5:"))


while number !=-1:
       total_number += number
       amount_inputted+= 1 
       number= int(input("Please say another number ")) 
       
if number==-1:
       print(total_number)

#calculate average of numbers before -1 was entered
    
if amount_inputted == 0:
       print("There is no solution as you cant divide by 0")
else:    
       average=total_number/amount_inputted
       print (average)




