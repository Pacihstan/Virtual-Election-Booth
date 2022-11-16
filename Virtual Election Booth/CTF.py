import os
# **********************************************************
# ***** CTF: Central Tabulating Facility functionality *****
# **********************************************************



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


class CTF:
    voterMessage = None
    matchFound = None
    isVotingBoothOpen = None
    candidates = []

    def __init__(self, name):
        self.name = name
        CTF.isVotingBoothOpen = True #Initialize to True
        



# This whole file ran on this while loop. Find a way to mimic this
#while isVotingBoothOpen:

    def ConstructVoterMessage():
        # Ask voter to enter name, valid_no, and vote
        print("What is your name?")
        name = input()
        print("Validation Number?")
        valid_no = input()
        # Candidate name must be spelled exactly for this prototype
        print("Who will you vote for? ")

        vote = input()

        # Create a Voter Message
        CTF.message = VoterMessage(name, valid_no, vote)

    def VerifyValidationNumber():
        # Check validation number against list received by the CLA
        # Open voterfile.txt
        f = open("voterfile.txt", "r")

        CTF.matchFound = False
        for line in f:
            # Read line
            currentLine = line.split(",")
            storedValidNo = currentLine[2].replace('\n', '')
            # If we find a match
            if CTF.message.valid_no == storedValidNo:
                # Match found, quit the loop
                CTF.matchFound = True

                # FIXME: Testing matching functionality
                print(f"Valid_no {storedValidNo} found!")
                CTF.message.bindSSN(currentLine[1])
                print(f"Voter's SSN is {CTF.message.SSN}")


        if not CTF.matchFound:
            # Reject vote message
            print("Could not find your validation number in the registered list. Please try again.")


        return CTF.matchFound

                

    def CheckIfValidationNoUsed():   
        # Check if the validation number is present in usednumbers.txt when the user
        #   enters their validation number.
        alreadyVoted = False

        if os.path.isfile("usednumbers.txt"):

            f = open("usednumbers.txt", "r")
            for line in f:
                currentLine = line.replace('\n', '')
                if CTF.message.valid_no == currentLine:
                    print("Voter's valid_no found in usednumbers. You cannot vote again.")
                    alreadyVoted = True
                    break
            f.close()

            return alreadyVoted

    def MarkValidationNoUsed():
        # If the validation number is present in voterfile.txt, "cross off" that number
        # Add the validation number to usednumbers.txt
        f = open("usednumbers.txt", "a")
        f.write(f"{CTF.message.valid_no}\n")
        f.close()

    def AddValidVote():
        # CTF adds the voter's SSN to the tally of one candidate
        # Create a new file, votes.txt, with the voter's candidate, SSN added as a line
        f = open("votes.txt", "a")
        f.write(f"{CTF.message.vote},{CTF.message.SSN}\n")
        f.close()

    def ValidationNumberNotFound():
        # Ask the voter to either enter their correct validation number, or leave
        print("Do you know your validation number? If so, enter 'y' to try to vote again.")
        print("Otherwise, enter 'n' to allow the next person to vote.")
        answer = input()

        return answer

    def CheckForMoreVoters():
        # Ask for more votes
        print("Are there any more voters? (y/n)")
        answer = input()
        if answer == 'n':
            isVotingBoothOpen = False
            print()  # newline
            return False

    def RecordVotes():
        # ********************************
        # ***** Final Count of Votes *****
        # ********************************

        # After all votes have been received, the CTF publishes the outcome
        # Tally up all the votes for each candidate in votes.txt

        # Have an empty list of Candidate objects
        # Each Candidate will have a name and vote_count
        CTF.candidates = []

        # Count the total number of votes
        totalNumOfVotes = 0

        # Open votes.txt
        f = open("votes.txt", "r")
        for line in f:
            currentLine = line.split(",")
            # Store the candidate's name
            nameOfCandidate = currentLine[0]

            # If the candidate is in the list, simply increment the vote count
            #    of that candidate
            candidateIsInList = False
            for candidate in CTF.candidates:
                if candidate.name == nameOfCandidate:
                    candidate.tallyVote()
                    totalNumOfVotes += 1
                    candidateIsInList = True
                    break

            # If the candidate is not in the list, add them with a default vote count of 1
            if not candidateIsInList:
                CTF.candidates.append(Candidate(nameOfCandidate))
                totalNumOfVotes += 1

    def PrintVotes():
        # Print out the tally of votes
        for candidate in CTF.candidates:
            print(candidate)