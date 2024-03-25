# creating lists and dictionairies to calcualte the stock and price of a cafe
# create a list called menu with items on it

menu=["coffee","panini", "chocolate cake", "sandwiches"]
print(menu)

stock_dict = {
    "coffee":8,
    "panini":12,
    "chocolate cake": 4,
    "sandwiches": 15

}
for x in stock_dict.items():
    print(x)


price_dict={
    "coffee":3.50,
    "panini": 5.50,
    "chocolate cake": 1.75,
    "sandwiches": 2.25
}

start=1 

indiv_value= {x:stock_dict[x] *  price_dict.get (x)
              for x in stock_dict.keys()}


print(indiv_value)

print("The total cost for each item on the menu is:" + str(indiv_value))