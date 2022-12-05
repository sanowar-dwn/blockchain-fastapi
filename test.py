import hashlib


def _to_digest(transactions):
    for i in transactions:
        to_digest = i.encode()
        print(to_digest)

    wto_digest = hashlib.sha256(to_digest).hexdigest()
    print(wto_digest)


_to_digest(['12', '13'])
