
from ape import project, networks


from .settings import *
from .addresses import *
from .accounts import *

def main():
    print("Load Contracts.. ")

def max_fee_calc():
    return "50 gwei"

def deploy_vouch(owner):

    vouch = project.Vouch.deploy( sender=owner, max_fee=max_fee_calc(), publish=publish())
    return vouch

def deploy_vouch_nft(owner, vouch):

    vouch_nft = project.VouchNFT.deploy( vouch, sender=owner, max_fee=max_fee_calc(), publish=publish())
    return vouch_nft

def deploy_bolivares_nft(owner):

    bolivares_nft = project.Bolivares.deploy( sender=owner, max_fee=max_fee_calc(), publish=publish())
    return bolivares_nft

