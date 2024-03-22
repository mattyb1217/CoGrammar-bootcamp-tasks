#  Calculate full holiday costs
#  Define functions with their parameters

# city_flight is the city the user is flying to
city_flight= "Bangkok"

# num_nights is the number of nights they are staying in the city
num_nights= 12

# rental_days is the amount of days the user will be renting a car for
rental_days= 8

num_nights= int(input( "welcome to Bangkok, the price per night is £75. How many nights are you staying?"))
print(num_nights)

price = 75

hotel_cost= num_nights * price
print(" The total cost is", hotel_cost)

# plane_cost is the cost of a flight to bangkok

city_flight= int(input("Flights to Bangkok are £600. How many tickets do you need?"))
print(city_flight)

ticket_price= 600

plane_cost= city_flight * ticket_price 
print("The total cost is £", plane_cost)



#car_rental is the cost to rent a car in bangkok

rental_days= int(input("The cost to rent a car is £10 a day. How many days are you renting a car for? "))
print(rental_days)

rental_price= 10

car_rental= rental_days * rental_price
print("The total cost is £", car_rental)

 

# holiday_cost is the total price including car_rental, plane_cost and hotel_cost
#num1= int(num_nights)
#num2= int(car_rental)
#num3= int(city_flight)

holiday_cost= hotel_cost + car_rental + plane_cost
print("Your total holiday cost is £",holiday_cost, "Enjoy your stay in Bangkok!!")





