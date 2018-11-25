from boa.interop.Neo.Storage import *
from boa.interop.Neo.Blockchain import *
from boa.interop.Neo.Header import *


ctx = GetContext()
# return unix timestamp
def getCurrentTime():
    height = GetHeight()
    header = GetHeader(height)
    timestamp = GetTimestamp(header)
    return timestamp


def setProposal(id, addr, title, content, token):
    expTime = token * 60 + getCurrentTime()
    # --------------------
    #0
    Put(ctx,id + '0', addr)
    #1
    Put(ctx,id + '1', title)
    #2
    Put(ctx,id + '2', content)
    #3
    Put(ctx,id + '3', token)
    #4
    Put(ctx,id + '4', expTime)
    #5 listOpponent
    Put(ctx, id + '5',"")
    #6 listAdvocate
    Put(ctx, id + '6',"")
    # ----------------------
    

    return True

def isExped(id):
    print("ahihi")
    if getCurrentTime() - Get(ctx, id + "4") > 0:
        return True
    return False
def upVote(id, voter):
    if isExped(id):
        return False
    if isVoted(id, voter):
        return False
    listUpVote = Get(ctx, id + '6') + voter
    Put(ctx, id + '6',listUpVote)
    return True
    
def downVote(id, voter):
    if isExped(id):
        return False
    if isVoted(id, voter):
        return False
    listDownVote = Get(ctx, id + '5') + voter
    Put(ctx, id + '6',listDownVote)
    return True

def isVoted(id, voter):
    if voter in Get(ctx, id + '5'):  
        return True
    if voter in Get(ctx, id + '6'):
        return True
    return False
def getProposal(id):
    proposer = Get(ctx, id + "0")
    title = Get(ctx, id + "1")
    content = Get(ctx, id + "2")
    token = Get(ctx, id + "3")
    expTime = Get(ctx, id + "4")
    listDownVote = Get(ctx,id + "5" )
    listUpVote = Get(ctx,id + "6" )
    return proposer + "_" + title + "_" + content + "_" + token + "_" + expTime + "_" + listDownVote + "_" + listUpVote

