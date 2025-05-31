import sys
sys.path.append('C:/Users/andre/PycharmProject/QCC')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256, merkle_root
from Blockchain.Backend.core.transaction import Transaction,Verification

import time
import json

ZERO_HASH='0'*64
VERSION=1
class Blockchain:
    def __init__(self):
        self.chain=[]
        self.GenesisBlock()

    def GenesisBlock(self):
        BlockHeight=0
        prevBlockHash=ZERO_HASH
        self.addBlock(BlockHeight,prevBlockHash)
    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp=int(time.time())
        Transaction=#verified_transaction
        merkleRoot=hash256(#verified_transactions.encode())
        bits='ffff001f'
        blockheader=BlockHeader(VERSION,prevBlockHash, merkleRoot,timestamp,bits)
        blockheader.mine()
        block=Block(BlockHeight,1,blockheader,1, Transaction)
        self.chain.append(block)
        print(json.dumps([b.to_dict() for b in self.chain], indent=4))

    def main(self, num_blocks=5):
        for _ in range(num_blocks):
            lastBlock=self.chain[-1] #access the last block
            BlockHeight=lastBlock.Height+1
            prevBlockHash=lastBlock.BlockHeader.blockHash
            self.addBlock(BlockHeight, prevBlockHash)

#create the blockchain instance
if __name__=="__main__":
    blockchain=Blockchain()
    blockchain.main(5)