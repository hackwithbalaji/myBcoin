from datetime import datetime;

print("Hey, its under development...")

class Block:
    def __init__(self,index, createdOn, data, hash = None, previousHash = None):
        self.index = index
        self.createdOn = createdOn
        self.data = data,
        self.hash = self.calculateHash(),
        self.previousHash = previousHash

    def calculateHash(self):
        return "Demo Hash " + str(self.index)

myFirstBlock = Block( 1, datetime.now(), { "price" : 100})
print(myFirstBlock.__dict__)