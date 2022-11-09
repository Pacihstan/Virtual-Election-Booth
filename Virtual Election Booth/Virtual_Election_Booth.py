# Import CLA file
# FIXME: How to prevent one voter from getting multiple validation numbers
from CLA import CLA

# Initialize isPollOpen to True
isPollOpen = True

while isPollOpen:
    # Ask the voter for name
    print("What is your name? ")
    name = input()
    cla = CLA(name)

    # Generates and outputs validation number
    validID = cla.generate_validation_num()
    print(f"{cla.name}, your validation number is: {validID}. Make sure to remember it.")

    # Write Name and Validation number on row in .txt file
    #with open('voterfile.txt', encoding='utf-8') as f:
    #    f.write("This is a test")
    f = open('voterfile.txt', 'a+', encoding="utf-8")
    f.write(f"{cla.name}, {validID}" + "\n")

    # Ask for more votes
    print("Are there any more voters? (y/n)")
    answer = input()
    if answer == 'n':
        isPollOpen = False

f.close()




if f.closed:
    print("voterfile is closed")
else:
    print("voterfile is still open")






