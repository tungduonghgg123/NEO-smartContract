from boa.interop.Neo.Blockchain import *
from boa.interop.Neo.Header import *



# return unix timestamp
def getCurrentTime():
    height = GetHeight()
    header = GetHeader(height)
    timestamp = GetTimestamp(header)
    return timestamp

listProposal = {1:2}

def setProposal(addr, title, content, token, proposal_id):
    proposal = {}
    expTime = token * 60 
    # --------------------
    #0
    proposal['addr'] = "tungduong"
    #1
    proposal['title'] = "tungduong"
    #2
    proposal['content'] = "tungduong"
    #3
    proposal['token'] = "tungduong"
    #4
    proposal['expTime'] = "tungduong"
    #5 listOpponent
    proposal['opponents'] = "tungduong"
    #6 listAdvocate
    proposal['advocates'] = "tungduong"
    #remove shit------------    
    # ----------------------
    listProposal[proposal_id] = proposal
    
    return True

def isExped(id):
    if getCurrentTime() - listProposal[id][4] > 0:
        return True
    return False
def upVote(id, voter):
    if not isExped(id):
        listProposal[id][6]
def downVote(id, voter):
    if not isExped(id):
        listProposal[id][5]

def isVoted(id, voter):
    if voter in listProposal[id][5]:
        return True
    if voter in listProposal[id][6]:
        return True
    return False
def getProposal(id):
    
    proposal = listProposal[id]
    print(proposal)
    return True
setProposal('AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','change the world','hello world',100, proposal_id = 1)
getProposal(1)