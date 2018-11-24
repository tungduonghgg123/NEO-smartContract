from nex.nep5 import *
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import *
from boa.interop.Neo.Blockchain import *
from boa.interop.Neo.Header import *


ctx = GetContext()
NEP5_METHODS = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer', 'transferFrom', 'approve', 'allowance']
creditPoints = {"":""}
initToken = {"",""}
class proposal:
    def __init__(self, addr, title, content, token)
    

def Main(operation, args1, args2):
    

    trigger = GetTrigger()

    # This is used in the Verification portion of the contract
    # To determine whether a transfer of system assets ( NEO/Gas) involving
    # This contract's address can proceed
    if trigger == Verification():
        print("verification step")
        # check if the invoker is the owner of this contract
        is_owner = CheckWitness(TOKEN_OWNER)

        # If owner, proceed
        if is_owner:
            print("is owner")
            return True
        print("not owner")
        return False

    elif trigger == Application():

        for op in NEP5_METHODS:
            if operation == op:
                return handle_nep51(ctx, operation, args1)

        if operation == 'setToken':
            return setToken(args1[0], args2[0])
        elif operation == 'bonusToken':
            return bonusToken(args1[0], args2[0])
        elif operation == 'minusToken':
            return minusToken(args1[0], args2[0])
        elif operation == 'getTime':
            return getCurrentTime()

        return 'unknown operation'

    return False
# return unix timestamp
def getCurrentTime():
    height = GetHeight()
    header = GetHeader(height)
    timestamp = GetTimestamp(header)
    return timestamp

#use this function when the semester starts, reset Token amount of every address
# haven't decentralized yet
def setToken(addr, amount):
    print("ahihi")
    if not CheckWitness(TOKEN_OWNER):
        print("Must be contract owner to set token")
        return False
    if amount <= 0:
        return False
    Put(ctx, addr, amount )

    return True


# user got more token 
def bonusToken(addr, amount):
    if not CheckWitness(TOKEN_OWNER):
        print("Must be contract owner to add token to user")
        return False
    if amount <= 0:
        return False
    current_amount = Get(ctx, addr)
    new_amount = current_amount + amount
    Put(ctx, addr,new_amount )
    return true

# only used by user
def minusToken(addr, amount):
    if not CheckWitness(addr):
        print("Must be owner to consume token")
        return False
    if amount <= 0:
        return False
    current_amount = Get(ctx, addr)
    new_amount = current_amount - amount
    if new_amount >= 0:
        Put(ctx, addr,new_amount )
        return true
    return false

def updateCreditPoint