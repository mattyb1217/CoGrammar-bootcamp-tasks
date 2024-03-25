#alternate cases of each letter
# ask for sentence to change cases
# find length of sentence for the alternate cases
# for every second letter type it upper case and every other letter lower case

first_string= input("Please enter a sentence here:") #"Come on you spurs"
list=[]

for a in range(len(first_string)):
    if a % 2 == 0:
        list.append(first_string[a].upper())
    else:
        list.append(first_string[a].lower())
print("" .join(list))


# alternate case of each word
# split and join needed to split the word into parts to change the cases
# join words back together specifying " " as the parameter for the join


second_string= input("Please enter another sentence:")
list2=[]

split_string= second_string.split()
print(split_string)

for a in range(len(split_string)):
    if a % 2 == 0:
        list2.append(split_string[a].upper())
    else:
        list2.append(split_string[a].lower())
print(" " .join(list2 ))







        



    

# sentence=first_string.upper()
# print(sentence)

# sentence.split()
# print(sentence.split())

# s="".join(split_string)
# print(s)