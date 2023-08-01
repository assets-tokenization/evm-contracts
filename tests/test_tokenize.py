# Import.
import pytest
from brownie import exceptions
from scripts.helpers import get_account, get_increased_gas_price
from scripts.deploy import deploy


# Constants.
TOKENIZE_COUNT = 10
TOKEN_GOV_REGISTRY_ID = "GOV_REGISTRY_ID_1"
TOKEN_NAME = "Apartment at 123 Main St."
TOKEN_DESCRIPTION = "The best apartment ever."


# Test can tokenize.
def test_can_tokenize():
    # Prepare.
    account = get_account()
    assets = deploy()

    # Tokenize.
    increased_gas_price = get_increased_gas_price()
    assets.tokenize(
        account.address,
        TOKEN_GOV_REGISTRY_ID,
        TOKEN_NAME,
        TOKEN_DESCRIPTION,
        {"from": account, "gas_price": increased_gas_price},
    ).wait(1)

    # Test tokenizd data.
    assert assets.getTokenOwner(1) == account.address
    assert assets.getTokenGovernmentRegistryId(1) == TOKEN_GOV_REGISTRY_ID


# Test can tokenize many.
def test_can_tokenize_many():
    # Prepare.
    account = get_account()
    assets = deploy()

    # Tokenize.
    increased_gas_price = get_increased_gas_price()
    for i in range(TOKENIZE_COUNT):
        assets.tokenize(
            account.address,
            TOKEN_GOV_REGISTRY_ID,
            TOKEN_NAME,
            TOKEN_DESCRIPTION,
            {"from": account, "gas_price": increased_gas_price},
        ).wait(1)

    # Test tokenizd data.
    for i in range(TOKENIZE_COUNT):
        assert assets.getTokenOwner(i + 1) == account.address
        assert assets.getTokenGovernmentRegistryId(i + 1) == TOKEN_GOV_REGISTRY_ID
