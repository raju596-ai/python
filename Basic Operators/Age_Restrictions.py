"""
Check if a user meets specific age criteria for an international car rental service.
Requirements:
Define an integer variable user_age.
Create a boolean variable can_rent that checks if user_age is greater than or equal to 21.
Create a second boolean variable needs_senior_insurance that checks if user_age is strictly greater than 70.
Test your code with user_age = 75 and print both boolean outcomes with clear labels.
"""



user_age = int(input("enter age : "))
can_rent = False
needs_senior_insurence = False

if user_age >= 21:
    can_rent = True
    if user_age > 70:
        can_rent = True
        needs_senior_insurence = True
    else:
        can_rent = True
        needs_senior_insurence = False


print(f"reant : {can_rent} \n insurence : {needs_senior_insurence}")


