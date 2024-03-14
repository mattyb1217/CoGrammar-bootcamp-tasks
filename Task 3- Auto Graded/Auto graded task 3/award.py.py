# create if else command depending on completion time
# define time
# use swimming, running and cycling times

swimming_time= input("What is your swimming_time?")
num1 = swimming_time
print(swimming_time)
 # use int(input("swimming time:"))

running_time= input("What is your running time")
num2= running_time
print(running_time)
 # use int(input("running time:"))

cycling_time = input("What is your cycling time")
num3= cycling_time
print(cycling_time)
 # use int(input("cycling time:"))

total= sum(num1, num2, num3) # total= swimming + running + cycling
print(total)

if total > 100: # = needed with >
    print( "awarded with provincial colours")