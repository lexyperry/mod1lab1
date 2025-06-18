pizza_size=input("small or large: ") #creating a customer input for pizza size
number_of_toppings=int(input("how many toppings do you want?")) #wrapping a input in a int so the return is an integer rather than a string
delivery_distance=int(input("Delievery distance in miles: "))#wrapping a input in a int so the return is an integer rather than a string
if pizza_size=="small":# if statement to calculate cost of pizza based on size
    base_cost=8
else:
    base_cost=12

cost_of_toppings=1*number_of_toppings #equation to calculate pizza cost based on # of toppings
def calculate_delivery_fee(delivery_distance):# additional cost equation based on delivery distance
    if delivery_distance <= 5: 
        return 2
    else:
        additional_miles=delivery_distance-5
        return 2+additional_miles*1
    
total_cost=base_cost+cost_of_toppings+calculate_delivery_fee(delivery_distance)
print(f"Total cost for your order is {total_cost}") #displaying total cost to user 