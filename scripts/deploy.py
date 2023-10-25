# Import.
from brownie import Assets
from scripts.helpers import (
    get_account_deploy,
    publish_source,
    get_increased_gas_price,
    CONTRACT_NAME,
    CONTRACT_SYMBOL,
    OWNER_CONTRACT,
    CONTRACT_DESCRIPTION,
    CONTRACT_REGISTRY_ID
)


# Deploy.
def deploy(owner_contract=OWNER_CONTRACT):
    account = get_account_deploy()
    incresed_gas_price = get_increased_gas_price()
    assets = Assets.deploy(
        CONTRACT_NAME,
        CONTRACT_SYMBOL,
        account.address,
        account.address,
        owner_contract,
        CONTRACT_DESCRIPTION,
        CONTRACT_REGISTRY_ID,
        {"from": account, "gas_price": incresed_gas_price},
        publish_source=publish_source(),
    )
    return assets


# Main.
def main():
    assets = deploy()
    return assets
