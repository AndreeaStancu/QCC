Merkle Tree
-createNode function
-insertNode function -not started  
-search/traverse tree - started to implement the function using depth first search, if the value that I'm searching for is found--> call the hash function and apply sha2. 
                      - I'm thinking if, in order to found the leaves I'm suppose to used DFS and an index, or if it will be better to use breath first search with queues(still learning) - and somehow apply the hashing function for the deepest level
                      
-hash function - sha2---> want to use post-quantum hash function SPINCS+. Hope to succeed
-combine hashes -not started --> staring from the bottom of the tree-> apply hash function for each individual leaf, and as we move to an upper layer, group them into a pair of 2 and apply hash func, up to the root--> root hash
                               
