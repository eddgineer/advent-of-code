from itertools import count
import hashlib

key = 'yzbqklnj'

make_hash = lambda key, nonce: hashlib.md5(f"{key}{nonce}".encode()).hexdigest()
verify_hash = lambda hash, difficulty: hash.startswith('0' * difficulty)

print(next(nonce for nonce in count() if verify_hash(make_hash(key, nonce), 5)))
print(next(nonce for nonce in count() if verify_hash(make_hash(key, nonce), 6)))