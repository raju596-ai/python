"""
Convert a total number of seconds into hours, minutes, and remaining seconds using division operators.
Requirements:
Define a variable total_seconds with an integer value (e.g., 9005).
Use floor division (//) to find the total hours.
Use the modulo operator (%) to find the remaining minutes and seconds.
Print the final output formatted exactly like this: 2 hours, 30 minutes, and 5 seconds.
proj

"""



total_seconds = 9005

hours = int(total_seconds / (60*60))

minitus = int((total_seconds - hours*(60*60)) / 60)
seconds = int((total_seconds -(hours * 3600) - minitus*60))

print(f"hours : {hours}, minitus : {minitus}, seconds : {seconds}")