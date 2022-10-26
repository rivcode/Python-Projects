# In this project, the program tells the user where in D.C. they are compared to some landmarks that they know
# Some of the landmarks include K St, The White House, Downing Hall, Dupont Circle, Union Station

# Assigning variables for the absolute coordinates of Downing Hall
downing_latitude = abs(38.921669)
downing_longitude = abs(-77.021361)

# Declaring input variables for absolute latitude and longitude values for the user
user_latitude = abs(float(input("Insert your latitude: ")))
user_longitude = abs(float(input("Insert your longitude: ")))

# Calculating differences in latitude and longitude
latitude_difference = abs(downing_latitude - user_latitude)
longitude_difference = abs(downing_longitude - user_longitude)

# Calculating the distance in miles using Pythagorean Theorm
distance = ( ((latitude_difference * 69) ** 2) + ((longitude_difference * 53) ** 2) ) ** 0.5

# Printing the distance to the nearest tenth of a mile
print("You are", round(distance, 1), "miles from Downing Hall")