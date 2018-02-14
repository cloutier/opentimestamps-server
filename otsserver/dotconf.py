import os

def getConfFileForChain(chainName):
    if chainName in ["mainnet", "regnet", "testnet"]:
        name = "bitcoin"
    elif chainName in ["litecoin", "litecoinTestnet"]:
        name = "litecoin"
    else:
        raise ValueError('Invalid chain name')

    return os.path.expanduser('~/.%s/%s.conf' % (name, name))

def getTickerForChain(chainName):
    if chainName in ["mainnet", "regnet", "testnet"]:
        return "BTC"
    elif chainName in ["litecoin", "litecoinTestnet"]:
        return "LTC"
    else:
        raise ValueError('Invalid chain name')

