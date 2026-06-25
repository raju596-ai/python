"""
Handle input conversion safely between user-facing text strings and mathematical numbers.
Requirements:
Start with two string variables: str_quantity = "12" and str_unit_price = "4.99".
Convert str_quantity into an integer and str_unit_price into a float.
Multiply them together to find the total_cost.
Print the data type of total_cost using the type() function, followed by its numerical value.
"""
str_quantity = "12"
st_unit_price = "4.99"

str_quantity = int(str_quantity)
st_unit_price = float(st_unit_price)

total_cost = str_quantity * st_unit_price

print(type(total_cost), total_cost)