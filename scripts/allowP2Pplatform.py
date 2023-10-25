# Import.
from brownie import Assets
from scripts.helpers import (
    publish_source,
    get_increased_gas_price,
    get_p2p_platform,
    P2P_PLATFORM,
    get_account_owner
)


# Deploy.
def AllowP2Pplatform(assets):
    account = get_account_owner()
    p2p_platform_account = get_p2p_platform()
    incresed_gas_price = get_increased_gas_price()
    assets.AllowP2Pplatform(
        p2p_platform_account.address,
        {"from": account, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    assets = Assets[-1]
    AllowP2Pplatform(assets)
    return assets
