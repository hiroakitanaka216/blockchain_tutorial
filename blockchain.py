import hashlib
import datetime
import os
import csv

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
        return Block(0, "2021/05/12", "Genesis block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock()["hash"]
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock.setdict())


def main():
    print("please input the number of the new blocks")
    num = int(input())
    index = 0
    coin = Blockchain()

    for i in range(num):
        if i==0:
            print("Please input the data")
        data = input()
        index += 1
        time = datetime.datetime.now().isoformat()
        coin.addBlock(Block(index, time, data))
    with open('blockchain_info.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(coin.chain)
        '''for j in range(len(coin.chain)):
            writer.writerow(coin.chain[j])'''


    print(coin.chain)

if __name__ == '__main__':
    main()
