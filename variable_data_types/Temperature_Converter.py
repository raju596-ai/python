""""Write a script that takes a temperature value and flips it to a new unit.
Requirements:
Define a variable celsius with a float value (e.g., 28.5).
Use the conversion formula: \(Fahrenheit = (Celsius \times \frac{9}{5}) + 32\).
Store the result in a variable called fahrenheit.
Print a string statement that dynamically includes both numbers (e.g., "28.5 degrees Celsius is 83.3 degrees Fahrenheit")
"""

celsius = 28.5

fehrenheit = (celsius*(9/5))+32

print(f"{celsius} degress celsius is {fehrenheit:.2f} degrees fehrenheit ")