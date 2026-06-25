"""
Determine if a user qualifies for a premium subscription based on their account age or balance.
Requirements:
Define account_age_months as an integer.Define wallet_balance as a float.
Create a boolean variable is_eligible that evaluates to True only if the account age is greater than 6 months OR the wallet balance is greater than or equal to 50.0.
Test it with account_age_months = 4 and wallet_balance = 75.50 and print the outcome of is_eligible."""

accounts_age_months = int(input("Enter the acount age : "))
wallet_balance = float(input("enter balance : "))

is_eligible = True

if accounts_age_months > 6 or wallet_balance > 50.0:

    is_eligible = True

else:
    is_eligible =False


print(is_eligible)
        