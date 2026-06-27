"""
Question 4: Nested Leap Year

 CheckerDetermine if a specific calendar year is a leap year using nested conditional checks.
 Requirements:
 Define an integer variable year.
 A year is a leap year if it is divisible by 4.
 Exception: If it is divisible by 100, it is not a leap year, unless it is also divisible by 400.
 Write this using nested if statements (an if inside another if).
 Test with year = 2000 (Leap) and year = 1900 (Not Leap).
"""

year = int(input("Enter a year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else : 
            print("not a leap year")

    else: 
        print("leap year")
else : 
    print("not a leap year")
