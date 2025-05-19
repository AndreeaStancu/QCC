from pymerkle import InmemoryTree as MerkleTree

# Create the tree
tree = MerkleTree(algorithm='sha256')

# Add entries
for data in [b'mere', b'pere', b'portocale', b'afine', b'zmeura']:
    tree.append_entry(data)

# Get hash of the first leaf
value = tree.get_leaf(3)
print(f"Leaf 3 - {value} hash")

# Get current tree size
size = tree.get_size()
print("Tree size:", size)

# Get current root hash
state = tree.get_state()
print("Current root hash:", state)

# Get root hash after 3 entries
state_3 = tree.get_state(3)
print("Root hash after 3 entries:", state_3)

# Generate inclusion proof (is leaf 2 included in version 3?)
proof = tree.prove_inclusion(2, 3)
print("Inclusion proof (leaf 2 in version 3):")
print(proof)
