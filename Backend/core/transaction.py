from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import binascii
import datetime
import collections
from utility.signature import verify_signature


class Client:
    def __init__(self):
        rng = Random.new().read
        self._private_key = RSA.generate(1024, rng)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == 'Genesis':
            identity = 'Genesis'
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.amount,
            'time': str(self.time)
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA256.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

def display_transaction(transaction):
    dict = transaction.to_dict()
    print("sender: " + dict['sender'])
    print('-----')
    print("recipient: " + dict['recipient'])
    print('-----')
    print("amount: " + str(dict['amount']))
    print('-----')
    print("time: " + dict['time'])
    print('-----')

#transaction queue--> append created transactions to this
transactions=[]

Mere = Client()
Caise = Client()
Zmeura = Client()
Capsuni = Client()

class Block:
    def __init__(self):
        #verified_transactions- only the verified transactions will be added to the block
        #transaction must be signed before it can be verified
        """
        Verified Transaction--> check that :
        -the digital signature is valid(it matches the sender public key)
        -the sender has enough funds
        -the transactions conforms to consensus rule
        """
        self.verified_transactions = []
        #store the previous hash-the chain of blocks becomes immutable
        self.previous_block_hash = ""


    #Create Genesis Block
    def genesis_block(self):
        Mere=Client()
        t0=Transaction("Genesis", Caise.identity, 500.0)
    #genesis transaction--> the first transaction recorder in the genesis block (Block 0) ,no previous transaction
        block0=Block() #create an instance of Block and call it block0
        block0.previous_block_hash=None
        Nonce=None
        block0.verified_transactions.append(t0)

class Verification:
    initial_balance = 1500  # Predefined balance for every new participant

    @staticmethod
    def verify_transaction(transaction, get_balance):
        # User identity
        sender_identity = transaction.sender.identity if hasattr(transaction.sender, 'identity') else transaction.sender

        # calculate balance
        sender_balance = Verification.initial_balance + get_balance(sender_identity)

        # Check funds
        if sender_balance < transaction.amount:
            print("Insufficient funds")
            return False

        # Verify the digital signature
        return verify_signature(
            sender_identity,
            transaction.signature,
            transaction.to_dict()
        )

    @staticmethod
    def verify_all_transactions(transactions, get_balance):
        verified_transactions = []
        for tx in transactions:
            if Verification.verify_transaction(tx, get_balance):
                verified_transactions.append(tx)
        return verified_transactions





#other transactions

t1 = Transaction(
    Mere,
    Caise.identity,
    15.0
)
t1.sign_transaction()
transactions.append(t1)
t2=Transaction(
    Caise,
    Zmeura.identity,
    23.0
)
t2.sign_transaction()
transactions.append(t2)
t3=Transaction(
    Capsuni,
    Mere.identity,
    28.0
)
t3.sign_transaction()
transactions.append(t3)

#display transactions
for transaction in transactions:
    display_transaction(transaction)