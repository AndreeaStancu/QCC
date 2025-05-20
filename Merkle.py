from pymerkle import InmemoryTree as MerkleTree
from pymerkle import verify_inclusion

def compute_root_hash(leaves):
    tree = MerkleTree(algorithm='sha256')
    for leaf in leaves:
        tree.append_entry(leaf)
    root = tree.get_state(5)
    return tree, root


def verify_proof():
    tree, root = compute_root_hash(leaves)
    proof = tree.prove_inclusion(3, 5)
    base = tree.get_leaf(3)
    test=verify_inclusion(base, root, proof)
    return test


leaves = [b'mere', b'pere', b'portocale', b'afine', b'zmeura']
tree, root = compute_root_hash(leaves)
print("Merkle Root:", root.hex())
try:
    verify_proof()
    print("Inclusion proof valid? True")
except InvalidProof:
    print("Inclusion proof valid? False")
