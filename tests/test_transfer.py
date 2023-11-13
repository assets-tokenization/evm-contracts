# Import.
import pytest
from brownie import exceptions
from scripts.helpers import get_account_deploy, get_account_owner, get_increased_gas_price, CONTRACT_REGISTRY_ID, OWNER_CONTRACT_NEW, get_account_shopper
from scripts.deploy import deploy
from scripts.addp2pplatformToList import AddP2pPplatform
from scripts.allowP2Pplatform import AllowP2Pplatform
from scripts.transferTokenByP2pPlatform import TransferTokenByP2pPlatform
from scripts.setDeal import setDeal
from scripts.acceptDeal import acceptDeal
from scripts.shopperListObjects import listDeal

from scripts.deploy_p2p import deploy_p2p

PRICE = '100000000000'


#Test can deploy


def test_deploy():
    p2p = deploy_p2p();
    account = get_account_deploy()
    asset = deploy(get_account_owner().address)

    print(asset);

    assert asset.getTokenOwner() == get_account_owner().address


def test_allowP2P():
    p2p = deploy_p2p();

    print(p2p)

def test_deal():
    p2p = deploy_p2p();
    account = get_account_deploy()
    asset = deploy(get_account_owner().address)

    assert asset.getTokenOwner() == get_account_owner().address

    AddP2pPplatform(asset, p2p)

    AllowP2Pplatform(asset, p2p)

    setDeal(PRICE, asset, get_account_shopper(), p2p)

    listDeal(get_account_shopper(), p2p)

    

def test_all():
    p2p = deploy_p2p();
    account = get_account_deploy()
    asset = deploy(get_account_owner().address)

    assert asset.getTokenOwner() == get_account_owner().address

    AddP2pPplatform(asset, p2p)

    AllowP2Pplatform(asset, p2p)

    setDeal(PRICE, asset, get_account_shopper(), p2p)

    myDeals = listDeal(get_account_shopper(), p2p)

    print('myDeals', myDeals)

    acceptDeal(asset, get_account_shopper(), p2p, PRICE)

