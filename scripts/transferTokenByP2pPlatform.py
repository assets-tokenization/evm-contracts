# Import.
from brownie import Assets
from scripts.helpers import (
    publish_source,
    get_increased_gas_price,
    get_p2p_platform,
    P2P_PLATFORM,
    OWNER_CONTRACT_NEW
)


# Deploy.
def TransferTokenByP2pPlatform(assets):
    incresed_gas_price = get_increased_gas_price()
    account = get_p2p_platform()
    assets.TransferTokenByP2pPlatform(
        OWNER_CONTRACT_NEW,
        {"from": account, "gas_price": incresed_gas_price}
    ).wait(1)


# Main.
def main():
    assets = Assets[-1]
    TransferTokenByP2pPlatform(assets)
    return assets
