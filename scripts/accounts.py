from ape import project, networks, accounts
from web3.middleware import geth_poa_middleware

from .settings import *

###########################################################
#  Accounts
###########################################################

def main():
    print("Load Accounts.. ")

# Return the ecosystem and network name 
def eco_network_name():
    ecosystem_name = networks.provider.network.ecosystem.name
    network_name = networks.provider.network.name
    return f"{ecosystem_name}:{network_name}"

# Loads accounts based on ecosystem and network
def load_accounts():
    if eco_network_name() in ['ethereum:mainnet']:
        # replace with your keys
        accounts.load("test1")

    if eco_network_name() in ['polygon:mainnet']:
        # replace with your keys
        accounts.load("test1")

    if eco_network_name() in ['ethereum:goerli']:
        # replace with your keys
        accounts.load("test1")
        networks.provider._web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    # add accounts if active network is goerli
    if eco_network_name() in ['polygon:mumbai']:
        # 0x
        # accounts.add('')
        accounts.load("test1")

    # if eco_network_name() in ['ethereum:local']:
    #     accounts[0].balance += int(100e18)

# Flag for determining etherscan publishing
def publish():
    if eco_network_name() in ['ethereum:local', 'polygon:mumbai']:
        return False
    else:
        return True