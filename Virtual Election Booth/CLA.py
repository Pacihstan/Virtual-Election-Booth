import random
import time
import os

# ************************************************************
# ***** CLA: Central Legitimization Agency functionality *****
# ************************************************************



class CLA:
    currentName = None
    voterSSN = None
    def __init__(self):
        pass

    def generate_validation_num():
        random.seed(time.time())
        validation_num = random.randint(1000000000000, 10000000000000)
        return validation_num

    def GetVoterInformation():
        # Ask the voter for name
        print("What is your name? ")
        CLA.currentName = input()
        # Ask voter for SSN
        print("What is your SSN?")
        CLA.voterSSN = input()

    def IS_SSNMatch():
        # Check if there is a match.
        f = open('ssnfile.txt', 'r', encoding="utf-8")

        # Check every line in ssnfile.txt
        ssnFound = False
        for line in f:
            # Read line
            currentLine = line.split(",")
            storedSSN = currentLine[1].replace('\n', '')
            # If we find a match
            if CLA.voterSSN == storedSSN:
                # Match found, quit the loop
                ssnFound = True
                break

        f.close()
        return ssnFound

    def GenerateValNoAndRecord():
        # Generate random validation number
        valid_no = CLA.generate_validation_num()
        print(f"{CLA.currentName}, your validation number is: {valid_no}. Make sure to remember it.")

        # Write Name and Validation number on row in .txt file
        f = open('voterfile.txt', 'a+', encoding="utf-8")
        f.write(f"{CLA.currentName},{CLA.voterSSN},{valid_no}" + "\n")
        f.close()

        # Set voterValidated to true
        voterValidated = True

    def AskIfMoreVoters():
        # Ask for more votes
        print("Are there any more voters? (y/n)")
        answer = input()
        if answer == 'n':
            return False
        else: return True