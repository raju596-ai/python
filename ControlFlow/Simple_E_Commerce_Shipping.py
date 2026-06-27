"""
Question 5: Simple E-Commerce Shipping Rules
Calculate shipping costs based on the order total and membership status.

Requirements:Define a float variable order_total = 45.0.
Define a boolean variable is_premium_member = False.
If is_premium_member is True, shipping is always 0.0.
If they are a regular member, shipping is 0.0 only if the order_total is $50.0 or more.
Otherwise, standard shipping is $7.50.Print the final shipping cost.
"""



order_total = 45.0
is_premium_member = False
shipping_cost = 0.0

if is_premium_member == True:
    shipping_cost = 0.0
elif order_total >= 50:
    shipping_cost = 0.0
else:
    shipping_cost = 7.50

print("total amount is : ",shipping_cost)
