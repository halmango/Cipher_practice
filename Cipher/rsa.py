from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

def readPEM(pemfile):
    h = open(pemfile, 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

def rsa_enc(msg):
    public_key = readPEM(r'C:\Users\USER\Documents\Python\publickey.pem')
    cipher = PKCS1_OAEP.new(public_key)
    encdata = cipher.encrypt(msg)
    return encdata

def rsa_dec(msg):
    private_key = readPEM(r'C:\Users\USER\Documents\Python\privatekey.pem')
    cipher = PKCS1_OAEP.new(private_key)
    decdate = cipher.decrypt(msg)
    return decdate

def main():
    msg = 'mint chocolate is not toothpaste'
    ciphered = rsa_enc(msg.encode('utf-8'))
    print(ciphered)
    deciphered = rsa_dec(ciphered)
    print(deciphered)

main()
