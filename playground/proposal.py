from boa.interop.Neo.Blockchain import *
from boa.interop.Neo.Header import *


# return unix timestamp
def getCurrentTime():
    height = GetHeight()
    header = GetHeader(height)
    timestamp = GetTimestamp(header)
    return timestamp

class proposal:
    def __init__(self, addr, title, content, token):
        self.title = title
        self.content = content
        # update to 86400
        self.expTime = token *60  + getCurrentTime
        self.token = token
        self.proposer = addr

        self.listOpponent = []


        self.listAdvocate = []

    def isExped(self):
        if(currentTime - self.expTime > 0)
            return True
        return False
    def upVote(self, voter):
        if not isExped():
            listAdvocate.append(voter)
    def downVote(self, voter):
        if not isExped():
            listOpponent.append(voter)
    
    def isVoted(self, voter):
        if voter in self.listOpponent:
            return True
        if voter in self.listAdvocate:
            return True
        return False
listProposal = []
# listProposal.append(proposal('AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y',"hello","hihi","SCL"))

    