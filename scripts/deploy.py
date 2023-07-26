# Import.
from brownie import Assets
from scripts.helpers import (
    get_account,
    publish_source,
    get_increased_gas_price,
    CONTRACT_NAME,
    CONTRACT_SYMBOL,
)


# Deploy.
def deploy():
    account = get_account()
    incresed_gas_price = get_increased_gas_price()
    assets = Assets.deploy(
        CONTRACT_NAME,
        CONTRACT_SYMBOL,
        account.address,
        account.address,
        {"from": account, "gas_price": incresed_gas_price},
        publish_source=publish_source(),
    )
    return assets


# Main.
def main():
    assets = deploy()
    return assets
