principle = float(input(" Enter amount : "))
rate = float(input("Enter rate of intrest : "))
years  = float(input("enter no of years : "))


amount = principle*(1 + rate)**years 
amount += 50
print(amount)