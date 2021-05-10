import hashlib


class Block:
    def __init__(self, index, timestamp, data, previousHash=""):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data;
        self.hash = self.calculateHash()

    def calculateHash(self):
        return (hashlib.sha256((str(self.index) + str(self.previousHash) + str(self.timestamp) + str(self.data)).encode(
            'utf-8')).hexdigest())

    def setdict(self):
        d = {"index": self.index, "previousHash": self.previousHash, "timestamp": self.timestamp, "data": self.data,
             "hash": self.hash}
        return d


class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock().setdict()]

    def createGenesisBlock(self):
        return Block(0, "2019/01/01", "Genesis block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock()["hash"]
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock.setdict())


def main():
    coin = Blockchain()

    coin.addBlock(Block(1, "2019/01/02", "amount: 10"))
    coin.addBlock(Block(2, "2019/01/03", "amount: 100"))
    coin.addBlock(Block(3, "2019/01/04", "amount: 1000"))

    print(coin.chain)


if __name__ == '__main__':
    main()
