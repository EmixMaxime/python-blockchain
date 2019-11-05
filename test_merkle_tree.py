from merkle_tree import MerkleTree

txHashes = [
  'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', # a
  '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d', # b
  '2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6', # c
  '18ac3e7343f016890c510e93f935261169d9e3f565436429830faf0934f4f8e4', # d
  '3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea' # e
]

def test_merkle():
    assert MerkleTree.merkle([]) == False
    assert MerkleTree.merkle(['aa']) == 'aa'
    assert MerkleTree.merkle(txHashes[:2]) == '62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154da'
    assert MerkleTree.merkle(txHashes[:3]) == '0bdf27bf7ec894ca7cadfe491ec1a3ece840f117989e8c5e9bd7086467bf6c38'
