import os
import hashlib
from hashlib import sha256 as sha
from base58check import b58encode
import ecdsa


def ripemd160(x):
    ret = hashlib.new('ripemd160')
    ret.update(x)
    return ret


def generateBitcoinAddress():
    privkey = os.urandom(32)
    fullkey = '80' + privkey.hex()

    a = bytes.fromhex(fullkey)
    sha_a = sha(a).digest()
    sha_b = sha(sha_a).hexdigest()
    c = bytes.fromhex(fullkey + sha_b[:8])

    WIF = b58encode(c)

    signing_key = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    pubkey = (verifying_key.to_string()).hex()

    pubkey = '04' + pubkey

    pub_sha = sha(bytes.fromhex(pubkey)).digest()
    encPubkey = ripemd160(pub_sha).digest()

    encPubkey = b'\x00' + encPubkey

    chunk = sha(sha(encPubkey).digest()).digest()

    checksum = chunk[:4]

    hex_address = encPubkey + checksum

    bitcoinAddress = b58encode(hex_address)

    print('+++WIF = ', WIF.decode())
    print('+++Bitcoin Address = ', bitcoinAddress.decode())


generateBitcoinAddress()
