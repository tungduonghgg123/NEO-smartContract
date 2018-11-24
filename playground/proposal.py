from boa.interop.Neo.Blockchain import *
from boa.interop.Neo.Header import *

listProposal = []

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
        self.expTime = token * 60  
        self.token = token
        self.proposer = addr
        self.index = len(listProposal) 
        self.listOpponent = []


        self.listAdvocate = []

    def isExped(self):
        if currentTime - self.expTime > 0:
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
    def get(self):
        print("proposer: ", self.proposer)
        print("title: ", self.title)
        print("content: ", self.content)
        print("expTime: ", self.expTime)
        print("token: ", self.token)
        print("index: ", self.index)
        print("listOpponent: ", self.listOpponent)
        print("listAdvocate: ", self.listAdvocate)

a = proposal("addr","title","content","token")
a.get()
# def setProposal(addr, title, content, token):
#     # a = proposal(addr,title,content,token)
#     # a = proposal("addr","title","content","token")
#     # listProposal.append()
#     return "success bro"
# print(setProposal("addr","title","content","token"))

# def getProposal(id):
#     listProposal[id].get()
#     return "success bro"
    