# Import.
from brownie import Assets
from scripts.helpers import (
    get_account,
    publish_source,
    get_increased_gas_price,
    P2P_PLATFORM
)


# Deploy.
def AddP2pPplatform(assets):
    account = get_account()
    incresed_gas_price = get_increased_gas_price()
    assets.AddP2pPplatform(
        P2P_PLATFORM,
        {"from": account, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    assets = Assets[-1]
    AddP2pPplatform(assets)
    return assets
