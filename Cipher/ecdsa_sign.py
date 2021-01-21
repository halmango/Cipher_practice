from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def readPEM_ECC(pem):
    with open(pem, 'r') as h:
        key = ECC.import_key(h.read())
    return key

def ecdsa_sign(msg):
    privateKey = readPEM_ECC(r'C:\Users\USER\Documents\Python\privkey_ecdsa.pem')
    sha = SHA256.new(msg)
    signer = DSS.new(privateKey, 'fips-186-3')
    signature = signer.sign(sha)
    return signature

def ecdsa_verify(msg, signature):
    publicKey = readPEM_ECC(r'C:\Users\USER\Documents\Python\pubkey_ecdsa.pem')
    sha = SHA256.new(msg)
    verifier = DSS.new(publicKey, 'fips-186-3')

    try:
        verifier.verify(sha, signature)
        print('Authentic')
    except ValueError:
        print('Not Authentic')

def main():
    msg = 'mint chocolate is not toothpaste'
    signature = ecdsa_sign(msg.encode('utf-8'))
    ecdsa_verify(msg.encode('utf-8'), signature)

main()
