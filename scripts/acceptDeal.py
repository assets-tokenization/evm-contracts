# Import.
from brownie import Assets, P2PPlatform
from scripts.helpers import (
    publish_source,
    get_increased_gas_price,
    get_p2p_platform,
    P2P_PLATFORM,
    get_account_owner
)


# Deploy.
def acceptDeal(asset, shopper,p2p):
    incresed_gas_price = get_increased_gas_price()
    p2p.acceptDeal(
        p2p.address,
        {"from": shopper, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    asset = Assets[-1]
    p2p = P2PPlatform[-1]
    acceptDeal(asset, get_account_shopper(), p2p)
    return assets
