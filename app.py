from datetime import datetime;
import hashlib;
import json;

print("Hey, its under development...")

class Block:
    def __init__(self,index, data, previousHash = None):
        self.index = index
        self.createdOn = str(datetime.now())
        self.data = data
        self.hash = self.calculateHash()
        self.previousHash = previousHash

    def calculateHash(self):
        return hashlib.sha256(
            json.dumps(self.__dict__).encode()
        ).hexdigest()

class BlockChain:
    def __init__(self):
        self.myBChain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block( 0, { "price" : 100})

    def addNewBlock(self, data):
        return self.myBChain.append(
            Block(len(self.myBChain), data, self.myBChain[len(self.myBChain) - 1].hash)
        )

myB = BlockChain()
myB.addNewBlock({"price" : 151})
for i in myB.myBChain:
    print(json.dumps(i.__dict__, indent=1))
    print("---------------------------------------------------------------------")