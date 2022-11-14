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


# Ask voter to enter name, valid_no, and vote
print("What is your name?")
name = input()
print("Validation Number?")
valid_no = input()
# FIXME: Candidate name must be spelled exactly for this prototype
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

# FIXME: Testing matching functionality
if not matchFound:
    print(f"Could not find a match")

f.close()

# If the validation number is present in voterfile.txt, "cross off" that number
# Add the validation number to usednumbers.txt
# FIXME: Have the program check if the validation number is present in usednumbers.txt when the user
#   enters their validation number (i.e., there is a match with voter file)
if matchFound:
    f = open("usednumbers.txt", "a")
    f.write(f"{message.valid_no}\n")

f.close()

# CTF adds the voter's SSN to the tally of one candidate
# Create a new file, votes.txt, with the voter's candidate, SSN added as a line
if matchFound:
    f = open("votes.txt", "a")
    f.write(f"{message.vote},{message.SSN}\n")

f.close()

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
















