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
    if(currentCLA.IS_SSNMatch()):
        if not currentCLA.IsNotAlreadyAVoter():
            currentCLA.GenerateValNoAndRecord()
        else:
            print("Voter has already registered...")
    else:
        print("Match not found...\n")

    isRegistrationOpen = currentCLA.AskIfMoreVoters()

print()  # newline
print("***** CTF: Central Tabulating Facility  *****")
#while is voting booth open
while(isVotingBoothOpen):
    
    currentCTF.ConstructVoterMessage() #Get Voter Message
    if (currentCTF.VerifyValidationNumber()):
        if (not currentCTF.CheckIfValidationNoUsed()):
            currentCTF.MarkValidationNoUsed()
            currentCTF.AddValidVote()
        else:
            continue
    else:
        continue

    isVotingBoothOpen = currentCTF.CheckForMoreVoters()

currentCTF.RecordVotes()
currentCTF.PrintVotes()
