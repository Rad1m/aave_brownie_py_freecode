from scripts.helpful_scripts import get_account, bcolors
from brownie import interface, config, network


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH
    """
    # ABI
    # Address
    account = get_account()
    val = 0.1
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": val * 10 ** 18})
    tx.wait(1)
    print(f"{bcolors.OKGREEN}\nReceived {val} WETH\n{bcolors.ENDC}")
    return tx
