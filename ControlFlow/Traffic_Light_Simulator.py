"""
Question 1: Traffic Light SimulatorSimulate
 a simple automated traffic light behavior using string inputs.
 Requirements:
 Define a string variable light_color (e.g., "yellow").
 Use an if-elif-else structure to check the color.
 If it is "red", print "Stop!".If it is "yellow", 
 print "Slow down!".If it is "green", 
 print "Go!".For any other text string, 
 print "Invalid traffic light color.".

"""

light_colour = input("Enter a colour")

if light_colour == "red":
    print("stop")

elif light_colour == "yellow":
    print("slow down!")
elif light_colour == "green":
    print("go")
else:
    print("Invalid trafic light colour")
