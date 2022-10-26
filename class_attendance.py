# In this project, the program lets students know if they are on-time or late based on their arrival time to class

# Asking a user to provide their arrival time in HH:MM format
arrival_time = input("Enter your arrival time in HH:MM format: ")

# Extracting hours and minutes
hours, minutes = arrival_time.split(":") 
# split(":") returns a list of strings splitting strings seperated by ":". 

# Converting string type hours to int type
hours = int(hours) 
# Converting string type minutes to int type
minutes = int(minutes) 

# Printing out what time the student arrived
print("You arrived at", str(hours) + ":" + str(minutes).zfill(2) + ".")

# Conditional to determine if a student is on-time or late
if (hours < 9 and minutes < 60) or (hours == 9 and minutes == 0):
  print("You are on time!")
elif hours >= 9 and minutes >= 12:
  print("You are late.")
  print("VERY late. Yikes.")
else:
  print("You are late.")