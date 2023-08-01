# Import.
from brownie import Assets
from scripts.helpers import get_account, get_increased_gas_price


# Constants.
TOKEN_GOV_REGISTRY_ID = "GOV_REGISTRY_ID_1"
TOKEN_NAME = "Apartment at 123 Main St."
TOKEN_DESCRIPTION = "The best apartment ever."


# Tokenize.
def tokenize(assets):
    account = get_account()
    increased_gas_price = get_increased_gas_price()
    assets.tokenize(
        account.address,
        TOKEN_GOV_REGISTRY_ID,
        TOKEN_NAME,
        TOKEN_DESCRIPTION,
        {"from": account, "gas_price": increased_gas_price},
    ).wait(1)


# Main.
def main():
    assets = Assets[-1]
    tokenize(assets)
    return assets
