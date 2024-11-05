# If Available_tickets is greater than sold_tickets then that is true
# Simple Expressions
# Condittion

trip_type = input("is your trip Business/leisure or personal?") .lower()
price = int(input("Expected trip cost:"))

discount = trip_type == 'businees' and price >= 1500

print("Customer receives a discount:", discount) 







# The basic of condittional statements
# The user 

code = input("Enter your code here:")

if code == "Winter23":
    print("You get a 20% discount!")
else:
    print("You don't get a discount")







