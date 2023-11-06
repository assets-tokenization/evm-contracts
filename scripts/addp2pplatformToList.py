# Import.
from brownie import Assets
from scripts.helpers import (
    get_account,
    get_account_owner,
    get_account_deploy,
    publish_source,
    get_increased_gas_price,
    P2P_PLATFORM
)


# Deploy.
def AddP2pPplatform(assets, p2p_platform):
    account = get_account_deploy()
    incresed_gas_price = get_increased_gas_price()
    assets.AddP2pPplatform(
        p2p_platform.address,
        {"from": account, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    assets = Assets[-1]
    AddP2pPplatform(assets, P2P_PLATFORM)
    return assets
