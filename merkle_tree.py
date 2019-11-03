import hashlib

class MerkleTree:
    # Hash pairs of items recursively until a single value is obtained
    @staticmethod
    def merkle(hashList):
        if len(hashList) == 1:
            return hashList[0]
        newHashList = []
        # Process pairs. For odd length, the last is skipped
        for i in range(0, len(hashList)-1, 2):
            newHashList.append(MerkleTree.hashRoot(hashList[i], hashList[i+1]))
        if len(hashList) % 2 == 1: # odd, hash last item twice
            newHashList.append(MerkleTree.hashRoot(hashList[-1], hashList[-1]))
        return MerkleTree.merkle(newHashList)

    @staticmethod
    def hashRoot(a, b):
        strTmp=(a+b)
        h = hashlib.sha256(strTmp.encode()).hexdigest()
        return h

    @staticmethod
    def merkleProof(txs, tx, proof = None):
        if proof is None:
            proof = []

        if len(txs) == 1:
            return proof
        tree = []

        for i in range(0, len(txs)-1, 2):
            tmpHash = MerkleTree.hashRoot(txs[i], txs[i+1])
            if txs[i] == tx:
                proof.append([1, txs[i+1]])
                tx = tmpHash
            elif txs[i+1] == tx:
                tx = tmpHash
                proof.append([0, txs[i]])
            tree.append(tmpHash)

        if len(txs) % 2 == 1: # odd, hash last item twice
            tmpHash = MerkleTree.hashRoot(txs[-1], txs[-1])
            if txs[i] == tx:
                proof.append([1, txs[-1]])
                tx = tmpHash
            tree.append(tmpHash)

        return MerkleTree.merkleProof(tree, tx, proof)

    @staticmethod
    def merkleProofRoot(root, proof, tx):
        tmpHash = tx
        for i in range(0, len(proof), 1):
            if proof[i][0] == 0:
                tmpHash = MerkleTree.hashRoot(proof[i][1], tmpHash)
            else:
                tmpHash = MerkleTree.hashRoot(tmpHash, proof[i][1])
        return root == tmpHash
                
