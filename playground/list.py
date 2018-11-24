from boa.builtins import list
from boa.compiler import Compiler

from boa.interop.Neo.Blockchain import *
from boa.interop.Neo.Header import *



# return unix timestamp
def getCurrentTime():
    height = GetHeight()
    header = GetHeader(height)
    timestamp = GetTimestamp(header)
    return timestamp

listProposal = []
def setProposal(addr, title, content, token):
    proposal = []
    expTime = token * 60 
    # --------------------
    #0
    proposal.append(addr)
    #1
    proposal.append(title)
    #2
    proposal.append(content)
    #3
    proposal.append(token)
    #4
    proposal.append(expTime)
    #5 listOpponent
    proposal.append([])
    #6 listAdvocate
    proposal.append([])
    # ----------------------
    listProposal.append(proposal)
    print(listProposal[0][0])
    print(listProposal[0][1])
    print(listProposal[0][2])
    print(listProposal[0][3])
    print(listProposal[0][4])
    print(listProposal[0][5])
    print(listProposal[0][6])

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
    # print("proposer: ", listProposal[id][0])
    # print("title: ", listProposal[id][1])
    # print("content: ", listProposal[id][2])
    # print("token: ", listProposal[id][3])
    # print("expTime: ", listProposal[id][4])
    # print("listOpponent: ", listProposal[id][5])
    # print("listAdvocate: ", listProposal[id][6])
    return True
setProposal('AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','change the world','hello world',100)
getProposal(0)


Compiler.load_and_save('path/to/your/file.py')