# ***** CLA: Central Legitimization Agency functionality *****

# Import CLA file
from CLA import CLA

# Initialize isRegistrationOpen to True
isRegistrationOpen = True

while isRegistrationOpen:
    # Ask the voter for name
    print("What is your name? ")
    name = input()
    cla = CLA(name)

    # Default condition assumes voter does not have an SSN
    voterValidated = False
    SSN = 0
    validID = 0
    while not voterValidated:
        # Ask voter for SSN
        print("What is your SSN?")
        SSN = input()

        # Check if there is a match.
        f = open('ssnfile.txt', 'r', encoding="utf-8")

        # Check every line in ssnfile.txt
        matchFound = False
        for line in f:
            # Read line
            currentLine = line.split(",")
            storedSSN = currentLine[1].replace('\n', '')
            # If we find a match
            if SSN == storedSSN:
                # Match found, quit the loop
                matchFound = True
                break

        f.close()

        # If match found
        if matchFound:
            # Generate random validation number
            validID = cla.generate_validation_num()
            print(f"{cla.name}, your validation number is: {validID}. Make sure to remember it.")

            # Set voterValidated to true
            voterValidated = True
        else:
            # Reject voter, ask for SSN again
            print("SSN invalid")

    # end of while not Validated

    # Write Name and Validation number on row in .txt file
    f = open('voterfile.txt', 'a+', encoding="utf-8")
    f.write(f"{cla.name},{SSN},{validID}" + "\n")

    # Ask for more votes
    print("Are there any more voters? (y/n)")
    answer = input()
    if answer == 'n':
        isRegistrationOpen = False

    f.close()

    if f.closed:
        print("voterfile is closed")
    else:
        print("voterfile is still open")

# end of while isRegistrationOpen

# ***** CTF: Central Tabulating Facility functionality *****







