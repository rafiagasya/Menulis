# Create a discount program
# Ask the user which type of trip they are taking
# Ask the user for an expected trip cost

trip_type = input("Is your trip Business/Leisure or personal? ").lower()
price = int(input("Expected trip cost: "))

discount = trip_type == 'business' and price >= 1200

print("Customer receives a discount:", discount)