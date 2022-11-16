# *********************************************************************
# README!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# THIS IS PROTOTYPE CODE! FINAL VERSION IS IMPLEMENTED IN
#  Virtual_Election_Booth.py
# ********************************************************************


import os

# ***** CTF: Central Tabulating Facility functionality *****

# Have voter create a voter message
class VoterMessage:
    def __init__(self, name, valid_no, vote):
        self.name = name
        self.valid_no = valid_no
        self.vote = vote

    def bindSSN(self, SSN):
        self.SSN = SSN


# Have a class representing a candidate and their votes
class Candidate:
    def __init__(self, name):
        self.name = name
        self.vote_count = 1 # default value

    def __str__(self):
        return f"{self.name}: {self.vote_count} votes"

    def tallyVote(self):
        self.vote_count += 1


# Initialize isVotingBoothOpen to True
isVotingBoothOpen = True

while isVotingBoothOpen:
    # Ask voter to enter name, valid_no, and vote
    print("What is your name?")
    name = input()
    print("Validation Number?")
    valid_no = input()
    # Candidate name must be spelled exactly for this prototype
    print("Who will you vote for? ")

    vote = input()

    # Create a Voter Message
    message = VoterMessage(name, valid_no, vote)

    # Check validation number against list received by the CLA
    # Open voterfile.txt
    f = open("voterfile.txt", "r")

    matchFound = False
    for line in f:
        # Read line
        currentLine = line.split(",")
        storedValidNo = currentLine[2].replace('\n', '')
        # If we find a match
        if message.valid_no == storedValidNo:
            # Match found, quit the loop
            matchFound = True

            # FIXME: Testing matching functionality
            print(f"Valid_no {storedValidNo} found!")
            message.bindSSN(currentLine[1])
            print(f"Voter's SSN is {message.SSN}")

            break

    if matchFound:
        # Check if the validation number is present in usednumbers.txt when the user
        #   enters their validation number.
        alreadyVoted = False
        if os.path.isfile("usednumbers.txt"):
            f = open("usednumbers.txt", "r")
            for line in f:
                currentLine = line.replace('\n', '')
                if message.valid_no == currentLine:
                    print("Voter's valid_no found in usednumbers. You cannot vote again.")
                    alreadyVoted = True
                    break
            f.close()

        # If the validation number is present in voterfile.txt, "cross off" that number
        # Add the validation number to usednumbers.txt
        if not alreadyVoted:
            f = open("usednumbers.txt", "a")
            f.write(f"{message.valid_no}\n")
            f.close()

            # CTF adds the voter's SSN to the tally of one candidate
            # Create a new file, votes.txt, with the voter's candidate, SSN added as a line
            f = open("votes.txt", "a")
            f.write(f"{message.vote},{message.SSN}\n")
            f.close()

    else:
        # Reject vote message
        print("Could not find your validation number in the registered list.")

        # Ask the voter to either enter their correct validation number, or leave
        print("Do you know your validation number? If so, enter 'y' to try to vote again.")
        print("Otherwise, enter 'n' to allow the next person to vote.")
        answer = input()

        if answer == 'y':
            # Ask voter to create a new voter message
            print("Please crate a new voter message...")
            print()  # newline
            continue

    f.close()

    # Ask for more votes
    print("Are there any more voters? (y/n)")
    answer = input()
    if answer == 'n':
        isVotingBoothOpen = False
        print() # newline
# endwhile

# *** Final Count of Votes ***

# After all votes have been received, the CTF publishes the outcome
# Tally up all the votes for each candidate in votes.txt

# Have an empty list of Candidate objects
# Each Candidate will have a name and vote_count
candidates = []

# Open votes.txt
f = open("votes.txt", "r")
for line in f:
    currentLine = line.split(",")
    # Store the candidate's name
    nameOfCandidate = currentLine[0]

    # If the candidate is in the list, simply increment the vote count
    #    of that candidate
    candidateIsInList = False
    for candidate in candidates:
        if candidate.name == nameOfCandidate:
            candidate.tallyVote()
            candidateIsInList = True
            break

    # If the candidate is not in the list, add them with a default vote count of 1
    if not candidateIsInList:
        candidates.append(Candidate(nameOfCandidate))


# Print out the tally of votes
for candidate in candidates:
    print(candidate)

# FIXME: Count actual voters out of registered votes (and print turnout percent?)
















