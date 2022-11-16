from CTF import CTF
from CLA import CLA
#import CLA
isVotingBoothOpen = True
isRegistrationOpen = True

# Print the name of the program for demonstration purposes
print("\n\nRunning Virtual_Election_Booth.py\n")

currentCLA = CLA
currentCTF = CTF

print("***** CLA: Central Legitimization Agency *****")
#while is registrationOpen
while(isRegistrationOpen):
    currentCLA.GetVoterInformation()
    if(currentCLA.IS_SSNMatch):
        currentCLA.GenerateValNoAndRecord()
    else:
        print("Match not found...\n")

    if not currentCLA.AskIfMoreVoters:
        isRegistrationOpen = False

print()  # newline
print("***** CTF: Central Tabulating Facility  *****")
#while is voting booth open
while(isVotingBoothOpen):
    
    currentCTF.ConstructVoterMessage() #Get Voter Message
    if (currentCTF.VerifyValidationNumber):
        if (not currentCTF.CheckIfValidationNoUsed()):
            currentCTF.MarkValidationNoUsed()
            currentCTF.AddValidVote()
        else:
            continue
    else:
        continue

    isVotingBoothOpen = CTF.CheckForMoreVoters

currentCTF.RecordVotes()
currentCTF.PrintVotes()
