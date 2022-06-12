from brownie import accounts,config, SimpleStorage
import os

def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account})
    store_value = simple_storage.retrieve()
    print(store_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    
def main():
    deploy_simple_storage()