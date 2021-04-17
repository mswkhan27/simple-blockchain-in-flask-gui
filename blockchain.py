import datetime
import hashlib


class Block:
    blockNo = 0
    data = None
    hash = ""
    previous_hash = ""
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data
        self.hash = self.hashing()

    def hashing(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(
            self.data) + "\nPrev Hash: " + str(self.previous_hash) + "\n--------------"


class Blockchain:
    chain = [Block("Genesis")]

    def __init__(self):
        self.chain = [Block("Genesis")]

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add(self, block):
        block.previous_hash = self.get_latest_block().hash
        block.blockNo += 1
        block.hash = block.hashing()
        self.chain.append(block)

    def isChainValid(self):
        i = 1
        while (i < len(self.chain)):

            prevBlock = self.chain[i - 1]
            currBlock = self.chain[i]
            if currBlock.hash != currBlock.hashing():
                return False

            if currBlock.previous_hash != prevBlock.hash:
                return False
            i += 1

        return True
