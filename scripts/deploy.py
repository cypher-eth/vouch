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
    ecosystem_name = networks.provider.network.ecosystem.name
    network_name = networks.provider.network.name
    provider_name = networks.provider.name
    click.echo(f"You are connected to network '{ecosystem_name}:{network_name}:{provider_name}'.")

def max_fee_calc():
    return "50 gwei"

#perk you can add args unlike main method
@click.command(cls=NetworkBoundCommand)
@ape_cli_context()
@network_option()
# cli_ctx must go first
def cli(cli_ctx, network):

    network_name = eco_network_name()
    print("network_name: ", network_name)
    load_accounts()
    print("account: ", accounts[0])
    now = datetime.now()
    network = cli_ctx.provider.network.name
    barcode_5 = "D03087656"
    barcode_50 = "Y02536574"
    barcode_500 = "Q59345550"
    if network == LOCAL_NETWORK_NAME or network.endswith("-fork"):
        owner = cli_ctx.account_manager.test_accounts[0]
        recipient = cli_ctx.account_manager.test_accounts[1]
        recipient2 = cli_ctx.account_manager.test_accounts[2]

    else:
        owner = accounts[0]
        recipient = "0x0C30403Bc4d0BdD6cbaC15E4499125AE6599aa23"
        recipient2 = "0x0C30403Bc4d0BdD6cbaC15E4499125AE6599aa23"

    # vouch = deploy_vouch(owner)
    # vouch.vouch(recipient,"Test", max_fee=max_fee_calc(), sender=owner)

    bolivares_nft = deploy_bolivares_nft(owner)
    # bolivares_nft.init(vouch, sender=owner, max_fee=max_fee_calc())
    bolivares_nft.register(recipient, barcode_5, sender=owner, max_fee=max_fee_calc())
    bolivares_nft.vouch(recipient, sender=owner, max_fee=max_fee_calc())

    # bolivares_nft.register(recipient2, barcode_50, sender=recipient, max_fee=max_fee_calc())
    # bolivares_nft.confirm(recipient2, barcode_50, 1, sender=owner, max_fee=max_fee_calc())
    # bolivares_nft.vouch(recipient2, sender=owner)

    print(bolivares_nft.verify(barcode_5));
    print(bolivares_nft.verify(barcode_50));

    print(owner)



