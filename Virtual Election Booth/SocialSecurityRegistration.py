import random
import time

# Print the name of the program for demonstration purposes
print("Running SocialSecurityRegistration.py\n")

# Ask what is your name
print("What is your name?")
name = input()

# Generate SSN
random.seed(time.time())
SSN = random.randint(100000000, 1000000000)

# Give user their SSN
print("Your social security number is: ")
print(SSN)

# Print SSN to file
f = open('ssnfile.txt', 'a+', encoding="utf-8")
f.write(f"{name},{SSN}" + "\n")

f.close()

