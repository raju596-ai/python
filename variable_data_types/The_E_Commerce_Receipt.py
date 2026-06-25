"""
Calculate the final price of an item after applying a discount and tax.
Requirements:
Define original_price as a float (e.g., 99.99).
Define discount_percent as an integer (e.g., 15 for 15%).
Define tax_percent as a float (e.g., 7.5 for 7.5%).
Calculate the discount amount, subtract it from the original price, and then add the calculated sales tax.
Print the final total rounded to 2 decimal places.

"""
original_price = 99.99
discount_percent = 15
tax_percent = 7.5


d_a = original_price *(discount_percent/100)
t_a = (original_price - d_a) *(tax_percent/100)
total = original_price - d_a + t_a

print(f"total : {total:.2f}")


