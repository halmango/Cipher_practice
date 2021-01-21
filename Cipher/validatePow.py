from hashlib import sha256 as sha
import codecs

def decodeBitCoinVal(bits):
    decode_hex = codecs.getdecoder('hex_codec')
    binn = decode_hex(bits) [0]
    ret = codecs.encode(binn[::-1], 'hex_codec')
    return ret

def getTarget(bits):
    bits = decodeBitCoinVal(bits)
    bits = int(bits, 16)
    bit1 = bits >> 4*6
    base = bits & 0x00ffffff

    sft = (bit1 - 0x3)*8
    target = base << sft
    return target

def validatePoW(header):
    block_version = header[0]
    hashPrevBlock = header[1]
    hashMerkleRoot = header[2]
    Time = header[3]
    Bits = header[4]
    nonce = header[5]

    decode_hex = codecs.getdecoder('hex_codec')
    header_hex = block_version + hashPrevBlock + hashMerkleRoot + Time + Bits + nonce
    header_bin = decode_hex(header_hex)[0]

    hash = sha(header_bin).digest()
    hash = sha(hash).digest()
    PoW = codecs.encode(hash[::-1], 'hex_codec')

    target = getTarget(Bits)
    target = str(hex(target))
    target = '0'*(66-len(target)) + target[2:]

    print('target\t=', target)
    print('BlockHash\t=', PoW.decode())

    if int(PoW, 16) <= int(target, 16):
        print("+++ Accept this Block")
    else:
        print("--- Reject this Block")

def main():
    block_version = '01000000'
    hashPrevBlock = '81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000'
    hashMerkleRoot = 'e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b'
    Time = 'c7f5d74d'
    Bits = 'f2b9441a'
    nonce = '42a14695'
    header = [block_version, hashPrevBlock, hashMerkleRoot, Time, Bits, nonce]
    validatePoW(header)
main()
