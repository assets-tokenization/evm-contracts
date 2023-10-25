# Import.
import pytest
from brownie import exceptions
from scripts.helpers import get_account_deploy, get_increased_gas_price, CONTRACT_REGISTRY_ID, OWNER_CONTRACT_NEW
from scripts.deploy import deploy
from scripts.addp2pplatformToList import AddP2pPplatform
from scripts.allowP2Pplatform import AllowP2Pplatform
from scripts.transferTokenByP2pPlatform import TransferTokenByP2pPlatform


# Constants.



# Test can tokenize.
def test_can_transfer():
    # Prepare.
    account = get_account_deploy()
    assets = deploy()

    # Add P2P Platform to list.
    increased_gas_price = get_increased_gas_price()
    AddP2pPplatform(assets)

    # Set P2P Platform as selected
    increased_gas_price = get_increased_gas_price()
    AllowP2Pplatform(assets)

    # Transfer to new owner
    increased_gas_price = get_increased_gas_price()
    TransferTokenByP2pPlatform(assets)


    # Test result owner.
    assert assets.getTokenOwner() == OWNER_CONTRACT_NEW
    assert assets.getTokenGovernmentRegistryId(1) == CONTRACT_REGISTRY_ID
