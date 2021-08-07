from datetime import datetime;
import hashlib;
import json;

print("Hey, its under development...")

class Block:
    def __init__(self,index, createdOn, data, previousHash = None):
        self.index = index
        self.createdOn = createdOn
        self.data = data,
        self.hash = self.calculateHash(),
        self.previousHash = previousHash

    def calculateHash(self):
        return hashlib.sha256(
            json.dumps(self.__dict__).encode()
        ).hexdigest()

myFirstBlock = Block( 1, str(datetime.now()), { "price" : 100})
print(myFirstBlock.__dict__)

class BlockChain:
    def __init__(self):
        self.myBChain = [self.createGenesisBlock()]

    def createGenesisBlock():
        return Block( 1, str(datetime.now()), { "price" : 100})
