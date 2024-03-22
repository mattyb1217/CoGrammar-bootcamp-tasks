# if else statement to create a pattern
# x+1 until x=4 then return back to 0
#input x as *
# if x =1
# need x multiplied by placement in loop

# Number_asked= int(input("Choose a number between 1 and 6 "))

x= "*"

for i in range(1,10):
    if i <=5:
        print(i * x)
    else: 
        y=10-i
        print(x*y)
                

