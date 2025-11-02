# Age Calculator using datetime module

import datetime 

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Get the current year from datetime
current_year = datetime.datetime.now().year

# Calculate age
age = current_year - birth_year

# Display the result
print(f"You are {age} years old.")

# Calculate and display years left to turn 100
years_left = 100 - age
print(f"You will turn 100 in {years_left} years!")