# Import.
from brownie import Assets
from scripts.helpers import (
    publish_source,
    get_increased_gas_price,
    P2P_PLATFORM,
    get_account_owner
)


# Deploy.
def AllowP2Pplatform(assets):
    account = get_account_owner()
    incresed_gas_price = get_increased_gas_price()
    assets.AllowP2Pplatform(
        P2P_PLATFORM,
        {"from": account, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    assets = Assets[-1]
    AllowP2Pplatform(assets)
    return assets
