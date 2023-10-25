# Import.
from brownie import accounts, config, network, web3


# Constants.
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

# Config params.
CONTRACT_NAME = config["constructor-args"]["contract_name"]
CONTRACT_SYMBOL = config["constructor-args"]["contract_symbol"]
OWNER_CONTRACT = config["constructor-args"]["owner_contract"]
OWNER_CONTRACT_NEW = config["p2p_platform-args"]["new_owner"]
CONTRACT_DESCRIPTION = config["constructor-args"]["contract_description"]
CONTRACT_REGISTRY_ID = config["constructor-args"]["contract_registry_id"]
P2P_PLATFORM = config["p2p_platform-args"]["allowed_p2p"]
GAS_PRICE_INCREASE_COEFFICIENT = float(config["gas_price_increase_coefficient"])


# Get account.
def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])

def get_account_deploy():
    return accounts[1]
    # return accounts.add(config["wallets"]["from_key"])

def get_account_owner():
    return accounts[2]
    # return accounts.add(config["wallets"]["owner"])

def get_p2p_platform():
    return accounts[3]

# Publish source indicator.
def publish_source():
    return config["networks"][network.show_active()].get("verify")


# Get increased gas price.
def get_increased_gas_price():
    gas_price = web3.eth.gas_price
    print(f"Gas price: {gas_price} wei")
    print(f"Gas price increase coefficient: {GAS_PRICE_INCREASE_COEFFICIENT}")
    incresed_gas_price = int(gas_price * GAS_PRICE_INCREASE_COEFFICIENT)
    print(f"Incresed gas price: {incresed_gas_price} wei")
    return incresed_gas_price
