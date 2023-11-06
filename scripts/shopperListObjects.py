# Import.
from brownie import P2PPlatform
from scripts.helpers import (
    publish_source,
    get_increased_gas_price,
    get_p2p_platform,
    P2P_PLATFORM,
    get_account_owner
)


# Deploy.
def listDeal(shopper,p2p):
    incresed_gas_price = get_increased_gas_price()
    p2p.myDeals(
        {"from": shopper, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    p2p = P2PPlatform[-1]
    listDeal(get_account_shopper(), p2p)
    return p2p
