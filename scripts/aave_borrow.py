from scripts.helpful_scripts import get_account, bcolors
from scripts.get_weth import get_weth
from brownie import config, network, interface
from web3 import Web3

# 0.1
AMOUNT = Web3.toWei(0.1, "ether")


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    print(f"{bcolors.WARNING}\nChecking blockchain network\n{bcolors.ENDC}")
    if network.show_active() in ["mainnet-fork"]:
        print(f"{bcolors.WARNING}\nUsing Mainnet-fork\n{bcolors.ENDC}")
        get_weth()
    else:
        print(f"{bcolors.WARNING}\nSkipping execution\n{bcolors.ENDC}")
