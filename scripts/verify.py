from ape import project, networks
from ape.cli import get_user_selected_account
import click
from ape.cli import network_option, NetworkBoundCommand, ape_cli_context, account_option
from ape.api.networks import LOCAL_NETWORK_NAME
from web3.middleware import geth_poa_middleware
from datetime import datetime

from .settings import *
from .addresses import *
from .accounts import *
from .contracts import *

# default connect to a provider
def main():
    etherscan = networks.provider.network.explorer
    etherscan.publish_contract("0x0000000000000000000000000000000000000000")

