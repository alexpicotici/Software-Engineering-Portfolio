# This program allows a user to calculate the cost for their holiday.

# Creating functions that will simplify the process:

# Calculate hotel cost:
def hotel_cost(nights: int, city: str) -> int:
    """
    Takes in an int value and multiplies it to the hotel cost.
    Returns the total cost.
    """
    if city.title() == "Paris":
        cost = int(nights) * 80
        return cost
    elif city.title() == "Bucharest":
        cost = int(nights) * 50
        return cost    
    elif city.title() == "London":
        cost = int(nights) * 100
        return cost    
    elif city.title() == "Milan":
        cost = int(nights) * 80
        return cost    
    elif city.title() == "Tokyo":
        cost = int(nights) * 60
        return cost    
    elif city.title() == "Manila":
        cost = int(nights) * 40
        return cost    
    elif city.title() == "New York":
        cost = int(nights) * 200
        return cost    


# Calculate plane cost:
def plane_cost(city: str) -> int:
    """
    Takes in a str value and assigns an int value to it.
    Returns the int value as the cost of the plane ticket.
    """
    if city.title() == "Paris":
        cost = 120
        return cost
    elif city.title() == "Bucharest":
        cost = 80
        return cost
    elif city.title() == "London":
        cost = 75
        return cost
    elif city.title() == "Milan":
        cost = 100
        return cost
    elif city.title() == "Tokyo":
        cost = 629
        return cost
    elif city.title() == "Manila":
        cost = 750
        return cost
    elif city.title() == "New York":
        cost = 555
        return cost
    

# Calculate the car rental cost:
def car_rental(days: int, city: str) -> int:
    """
    Takes in the number of days(int) and multiplies it to the city car
    hire rate. 
    Returns total cost(int value).
    """
    if city.title() == "Paris":
        cost = int(days) * 25
        return cost
    elif city.title() == "Bucharest":
        cost = int(days) * 14
        return cost
    elif city.title() == "London":
        cost = int(days) * 30
        return cost
    elif city.title() == "Milan":
        cost = int(days) * 30
        return cost
    elif city.title() == "Tokyo":
        cost = int(days) * 45
        return cost
    elif city.title() == "Manila":
        cost = int(days) * 20
        return cost
    elif city.title() == "New York":
        cost = int(days) * 35
        return cost


# Calculate the total holiday cost:
def holiday_cost(hotel: int, plane: int, car:int) -> int:
    """
    takes in the hotel cost value, plane cost value, car hire 
    value(int). Calculates total value.
    Returns total holiday cost value(int).
    """
    total_cost = int(plane) + int(hotel) + int(car)
    return total_cost


"""
The user will be asked to provide their destination city, the number of
nights they will be staying in hotels, and the number of days they will 
be using a rented car.
"""
# List of city destinations that the user can choose from:
city_list = ["Paris", "Bucharest", "London", "Milan", "Tokyo", "Manila",
              "New York"]
city_flight = input("""Please select a destination city from this list:
                    Paris
                    Bucharest
                    London
                    Milan
                    Tokyo
                    Manila
                    New York
                    \nType the name of the city in this box:\n """)

# Raise a TypeError if user enters invalid input.
if city_flight.title() not in city_list:
    raise TypeError("""You have not selected a valid option. Please start
again, and select a valid destination!""")

num_nights = input("How many nights will you be needing a hotel for?:\n ")
rental_days = input("How many days will you need to rent a car for?:\n ")


# Calling the functions and calculating the total holiday cost:
hotel_spending = hotel_cost(num_nights, city_flight)
flight_spending = plane_cost(city_flight)
car_spending = car_rental(rental_days, city_flight)
holiday_total_spending = holiday_cost(hotel_spending, flight_spending, car_spending)

# Printing the final result:
print(f"""\nYou will be travelling to {city_flight.title()}. The tickets 
will cost you £{str(flight_spending)}, the hotel will cost you 
£{str(hotel_spending)}, and the car hire will cost you £{str(car_spending)}.
In total, you will need a budget of £{str(holiday_total_spending)} for your
holiday.
Don't forget your passport!
""")
