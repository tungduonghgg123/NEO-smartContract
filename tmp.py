
from nex.txio import get_asset_attachments
from nex.token import *
from nex.crowdsale import *
from nex.nep5 import *
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import *

ctx = GetContext()
NEP5_METHODS = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer', 'transferFrom', 'approve', 'allowance']


def Main(operation, args1, args2):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """

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
        # Otherwise, we need to lookup the assets and determine
        # If attachments of assets is ok
        attachments = get_asset_attachments()
        return can_exchange(ctx, attachments, True)

    elif trigger == Application():

        for op in NEP5_METHODS:
            if operation == op:
                return handle_nep51(ctx, operation, args)

        if operation == 'deploy':
            return deploy()
        elif operation == 'set':
            return setToken(args1, args2)
        return 'unknown operation'

    return False

def setToken(addr, amount):
    if not CheckWitness(TOKEN_OWNER):
        print("Must be owner to set token to addresses")
        return False
    for i in range(len(addr)):
        Put(ctx, addr[i], amount[i])
        return True
    
# def deploy():
#     """

#     :param token: Token The token to deploy
#     :return:
#         bool: Whether the operation was successful
#     """
#     if not CheckWitness(TOKEN_OWNER):
#         print("Must be owner to deploy")
#         return False

#     if not Get(ctx, 'initialized'):
#         # do deploy logic
#         Put(ctx, 'initialized', 1)
#         Put(ctx, TOKEN_OWNER, TOKEN_INITIAL_AMOUNT)
#         return add_to_circulation(ctx, TOKEN_INITIAL_AMOUNT)

#     return False

