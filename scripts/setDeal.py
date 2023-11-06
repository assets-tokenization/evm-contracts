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
def setDeal(price, asset, shopper,p2p):
    account = get_account_owner()
    incresed_gas_price = get_increased_gas_price()
    p2p.setDeal(
        price,
        asset.address,
        shopper.address,
        {"from": account, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    asset = Assets[-1]
    p2p = P2PPlatform[-1]
    setDeal('1000000000000', asset, get_account_shopper(), p2p)
    return assets
