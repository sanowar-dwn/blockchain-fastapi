import hashlib

transactions = ['12', '123', '124', '125']
len_transactions = len(transactions)
hashed_transactions = []

def _to_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

for i in range(len_transactions):
    x = _to_hash(transactions[i])
    hashed_transactions.append(x)


def get_merkle_root(encoded_transactions):
    left_node = _to_hash(encoded_transactions[0] + encoded_transactions[1])
    right_node = _to_hash(encoded_transactions[2] + encoded_transactions[3])
    print(_to_hash(left_node + right_node))


get_merkle_root(hashed_transactions)
