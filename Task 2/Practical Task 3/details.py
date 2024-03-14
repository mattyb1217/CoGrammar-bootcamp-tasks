# Finding the name, age and address of a user using the input() command
# Use input() to ask for their name, age, house number and road name
# Print the answer to each question right after.

Name= input("What is your name?")
print(Name)

Age= input("What is your age?")
print(Age)

Address1= input("What is your house number?")
Address2= input("What is your road name?")
print(Address1 + Address2)

# When all questions are answered write a sentence including all the answers using print() command
print (Name + " is " +  Age +  " years old. " + " They live at " + Address1 +   Address2)