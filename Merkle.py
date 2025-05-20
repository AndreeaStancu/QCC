from pymerkle import InmemoryTree as MerkleTree

def compute_root_hash(leaves):
    tree = MerkleTree(algorithm='sha256')
    for leaf in leaves:
        tree.append_entry(leaf)
    root_hash = tree.get_state()
    return root_hash.hex()

leaves = [b'mere', b'pere', b'portocale', b'afine', b'zmeura']
print("Merkle Root:", compute_root_hash(leaves))
