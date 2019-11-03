from blockchain_factory import blockchain_factory

try:
    bc, network = blockchain_factory()
except BaseException as error:
    print('An exception occurred: {}'.format(error))
    network.stop()
