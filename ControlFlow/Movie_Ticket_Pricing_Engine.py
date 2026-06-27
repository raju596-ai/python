"""
Question 3: Movie Ticket Pricing EngineCalculate 

the ticket cost for a cinema based on a customer's age.
Requirements:
Define an integer variable age and a float variable base_price = 12.0.
If the customer is a child (age under 12),  they get a 50% discount.
If they are a senior citizen (age of 65 or older), they get a 25% discount.
Everyone else pays the full base_price.
Calculate and print the final ticket price based on the condition met.
"""


age  = int(input("enter age : "))
base_price = 12.0

if age < 12:
    base_price -= base_price*(50/100)
elif age > 65 :
    base_price -= base_price*(25/100)
else:
    base_price

print("need to pay : ", base_price)