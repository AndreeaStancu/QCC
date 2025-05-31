class Block:
    """
    Block is a storage container that stores transactions

    """

    def __init__(self, Height, Blocksize, BlockHeader,TxCount,Txs):
        self.Height=Height
        self.Blocksize=Blocksize
        self.BlockHeader=BlockHeader
        self.TxCount=TxCount #number of transactions
        self.Txs=Txs #transaction itself

    def to_dict(self):
        return{
            "height":self.Height,
            "header":self.BlockHeader.to_dict() if hasattr(self.BlockHeader, "to_dict") else self.BlockHeader,
            "txnCount":self.TxCount,
            "txn":self.Txs
        }
