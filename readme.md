# Blockchain Class Documentation

The `Blockchain` class is a simple implementation of a blockchain data structure. It provides basic functionality for creating blocks, mining blocks, and validating the integrity of the blockchain. The class also includes additional methods for managing coins and generating public addresses.

## Class Methods

### `__init__()`
The constructor method initializes the `Blockchain` object by creating the initial block, also known as the "genesis block". It sets up an empty list to hold the chain and appends the genesis block to the chain.

### `mine_block(data: str) -> dict`
The `mine_block()` method creates a new block and adds it to the blockchain. It takes a `data` parameter, which represents the data to be stored in the new block. The method calculates the proof of work, previous hash, and index for the block and creates a new block using the `_create_block()` method. The new block is then appended to the chain, and the method returns the newly created block.

### `_create_block(data: str, proof: int, previous_hash: str, index: int) -> dict`
The `_create_block()` method is a private method that creates a new block with the provided data, proof, previous hash, and index. It returns the newly created block as a dictionary.

### `get_previous_block() -> dict`
The `get_previous_block()` method returns the previous block in the chain. It retrieves the last block from the chain list and returns it.

### `get_genesis_block() -> dict`
The `get_genesis_block()` method returns the genesis block, which is the first block in the chain. It retrieves the first block from the chain list and returns it.

### `get_coins()`
The `get_coins()` method returns the total number of coins in the blockchain. In this implementation, it always returns a fixed value of 12.

### `generate_public_address()`
The `generate_public_address()` method generates a new public address using the `bitcoinaddress` library. It creates a new `Wallet` object and retrieves the public address associated with the testnet. The method returns the generated public address as a string.

### `_to_digest(new_proof: int, previous_proof: int, index: int, data: str) -> bytes`
The `_to_digest()` method calculates the digest of the given parameters. It takes the new proof, previous proof, index, and data as inputs and returns the encoded digest as bytes.

### `_proof_of_work(previous_proof: str, index: int, data: str) -> int`
The `_proof_of_work()` method performs the proof of work algorithm to find a valid proof for the new block. It takes the previous proof, index, and data as inputs and iteratively searches for a proof that satisfies a specific condition (in this case, a hash with leading zeros). The method returns the valid proof as an integer.

### `_hash(block: dict) -> str`
The `_hash()` method calculates the cryptographic hash of a given block. It takes a block dictionary as input, serializes it into a JSON string, encodes the string, and then computes the SHA256 hash of the encoded block. The method returns the hash value as a string.

### `is_chain_valid() -> bool`
The `is_chain_valid()` method checks the validity of the entire blockchain. It iterates over each block in the chain and verifies the integrity of the blocks and the correctness of their proofs of work. The method returns `True` if the chain is valid and `False` otherwise.

## Example Usage

```python
# Create a new instance of the Blockchain class
blockchain = Blockchain()

# Mine a new block
blockchain.mine_block("Some data")

# Get the previous block
previous_block = blockchain.get_previous_block()

# Get the total number of coins in the blockchain
total_coins = blockchain.get_coins()

# Generate a new public address
public_address = blockchain.generate_public_address()

# Check the validity of the blockchain
is_valid = blockchain.is_chain_valid()
