import hashlib

def hash256(s):
    """
    Two rounds of SHA256
    """
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

def merkle_parent_level(hashes):
    """takes a list of binary hashes and return a list that's half of the lenght"""
    #computes the parent level in a merkle tree given a list of child nodes(hashes)
    if len(hashes)%2==1:  #if odd number of hashes
        hashes.append(hashes[-1]) #duplicate the last hash to make the list even(standard practice in merkle treese)

    parent_level=[] # an empty list to hold the parent hashes

    for i in range(0, len(hashes), 2): #iterate in pairs(0&1, 2&3..),
        parent=hash256(hashes[i] +hashes[i+1]) #concatenate them,compute their hash
        parent_level.append(parent) #append result to parent_level
    return parent_level #return the list of parent_level

def merkle_root(hashes):
    """
    Takes a list of binary hashes and return the merkle root
    """
    #recursively calculates the Merkle root, the single top-level hash that summarizes all the data
    current_level=hashes  #start the list of input hashes
    while len(current_level)>1:  #loop until a single hash remains
        current_level=merkle_parent_level(current_level)

    return current_level#return the last element



