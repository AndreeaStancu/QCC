import hashlib
from Blockchain.Backend.util.util import hash256

class BlockHeader:
    def __init__(self,version,prevBlockHash, merkleRoot, timestamp,bits):
        self.version=version
        self.prevBlockHash=prevBlockHash
        self.merkleRoot=merkleRoot
        self.timestamp=timestamp
        self.bits=bits  #target difficulty
        self.nonce=0
        self.blockHash=''

    def to_dict(self):
        return{
            "version":self.version,
            "prevBlockHash":self.prevBlockHash,
            "merkleRoot":self.merkleRoot.hex() if isinstance(self.merkleRoot, bytes) else self.merkleRoot,
            "timestamp":self.timestamp,
            "bits":self.nonce,
            "blockHash":self.blockHash
        }


    def mine(self):
        print("Mining Started...")

        while not self.blockHash.startswith('00'):
            header=(
                f"{self.version}"
                f"{self.prevBlockHash}"
                f"{self.merkleRoot}"
                f"{self.timestamp}"
                f"{self.bits}"
                f"{self.nonce}"
            )
            self.blockHash = hashlib.sha256(header.encode()).hexdigest()
            self.nonce+=1

            print(f"Trying nonce: {self.nonce}", end='\r')
        print(f"\nBlock mined! Nonce: {self.nonce}, Hash: {self.blockHash}")
