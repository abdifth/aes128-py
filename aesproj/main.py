import pandas as pd
import numpy as np

while True:
    message = input("enter message: ")
    assert len(message) <= 16
    if len(message.strip()) == 0 or message.count(' ') > 0:
        print("cant do empty input or spaces")
    else:
        break

while len(message) < 16:
    message += "n"

while True:
    key = input("enter key: ")
    assert len(key) <= 16

    if len(key.strip()) == 0 or key.count(' ') > 0:
        print("space detected retry")
    else:
        break

while len(key) < 16:
    key += "n"

# print(message, key)

np.set_printoptions(formatter={'int': hex})

x = [ord(m) for m in message]
y = [ord(k) for k in key]

keyArr = (np.reshape(y, (4, 4))).T

j = np.bitwise_xor(x, y)
startRound = np.reshape(j, (4, 4)).T
# mprint(startRound)

Sbox = {
    0x00: 0x63, 0x01: 0x7C, 0x02: 0x77, 0x03: 0x7B, 0x04: 0xF2, 0x05: 0x6B, 0x06: 0x6F, 0x07: 0xC5, 0x08: 0x30,
    0x09: 0x01, 0x0a: 0x67, 0x0b: 0x2B, 0x0c: 0xFE, 0x0d: 0xD7, 0x0e: 0xAB, 0x0f: 0x76,
    0x10: 0xCA, 0x11: 0x82, 0x12: 0xC9, 0x13: 0x7D, 0x14: 0xFA, 0x15: 0x59, 0x16: 0x47, 0x17: 0xF0, 0x18: 0xAD,
    0x19: 0xD4, 0x1a: 0xA2, 0x1b: 0xAF, 0x1c: 0x9C, 0x1d: 0xA4, 0x1e: 0x72, 0x1f: 0xC0,
    0x20: 0xB7, 0x21: 0xFD, 0x22: 0x93, 0x23: 0x26, 0x24: 0x36, 0x25: 0x3F, 0x26: 0xF7, 0x27: 0xCC, 0x28: 0x34,
    0x29: 0xA5, 0x2a: 0xE5, 0x2b: 0xF1, 0x2c: 0x71, 0x2d: 0xD8, 0x2e: 0x31, 0x2f: 0x15,
    0x30: 0x04, 0x31: 0xC7, 0x32: 0x23, 0x33: 0xC3, 0x34: 0x18, 0x35: 0x96, 0x36: 0x05, 0x37: 0x9A, 0x38: 0x07,
    0x39: 0x12, 0x3a: 0x80, 0x3b: 0xE2, 0x3c: 0xEB, 0x3d: 0x27, 0x3e: 0xB2, 0x3f: 0x75,
    0x40: 0x09, 0x41: 0x83, 0x42: 0x2C, 0x43: 0x1A, 0x44: 0x1B, 0x45: 0x6E, 0x46: 0x5A, 0x47: 0xA0, 0x48: 0x52,
    0x49: 0x3B, 0x4a: 0xD6, 0x4b: 0xB3, 0x4c: 0x29, 0x4d: 0xE3, 0x4e: 0x2F, 0x4f: 0x84,
    0x50: 0x53, 0x51: 0xD1, 0x52: 0x00, 0x53: 0xED, 0x54: 0x20, 0x55: 0xFC, 0x56: 0xB1, 0x57: 0x5B, 0x58: 0x6A,
    0x59: 0xCB, 0x5a: 0xBE, 0x5b: 0x39, 0x5c: 0x4A, 0x5d: 0x4C, 0x5e: 0x58, 0x5f: 0xCF,
    0x60: 0xD0, 0x61: 0xEF, 0x62: 0xAA, 0x63: 0xFB, 0x64: 0x43, 0x65: 0x4D, 0x66: 0x33, 0x67: 0x85, 0x68: 0x45,
    0x69: 0xF9, 0x6a: 0x02, 0x6b: 0x7F, 0x6c: 0x50, 0x6d: 0x3C, 0x6e: 0x9F, 0x6f: 0xA8,
    0x70: 0x51, 0x71: 0xA3, 0x72: 0x40, 0x73: 0x8F, 0x74: 0x92, 0x75: 0x9D, 0x76: 0x38, 0x77: 0xF5, 0x78: 0xBC,
    0x79: 0xB6, 0x7a: 0xDA, 0x7b: 0x21, 0x7c: 0x10, 0x7d: 0xFF, 0x7e: 0xF3, 0x7f: 0xD2,
    0x80: 0xCD, 0x81: 0x0C, 0x82: 0x13, 0x83: 0xEC, 0x84: 0x5F, 0x85: 0x97, 0x86: 0x44, 0x87: 0x17, 0x88: 0xC4,
    0x89: 0xA7, 0x8a: 0x7E, 0x8b: 0x3D, 0x8c: 0x64, 0x8d: 0x5D, 0x8e: 0x19, 0x8f: 0x73,
    0x90: 0x60, 0x91: 0x81, 0x92: 0x4F, 0x93: 0xDC, 0x94: 0x22, 0x95: 0x2A, 0x96: 0x90, 0x97: 0x88, 0x98: 0x46,
    0x99: 0xEE, 0x9a: 0xB8, 0x9b: 0x14, 0x9c: 0xDE, 0x9d: 0x5E, 0x9e: 0x0B, 0x9f: 0xDB,
    0xa0: 0xE0, 0xa1: 0x32, 0xa2: 0x3A, 0xa3: 0x0A, 0xa4: 0x49, 0xa5: 0x06, 0xa6: 0x24, 0xa7: 0x5C, 0xa8: 0xC2,
    0xa9: 0xD3, 0xaa: 0xAC, 0xab: 0x62, 0xac: 0x91, 0xad: 0x95, 0xae: 0xE4, 0xaf: 0x79,
    0xb0: 0xE7, 0xb1: 0xC8, 0xb2: 0x37, 0xb3: 0x6D, 0xb4: 0x8D, 0xb5: 0xD5, 0xb6: 0x4E, 0xb7: 0xA9, 0xb8: 0x6C,
    0xb9: 0x56, 0xba: 0xF4, 0xbb: 0xEA, 0xbc: 0x65, 0xbd: 0x7A, 0xbe: 0xAE, 0xbf: 0x08,
    0xc0: 0xBA, 0xc1: 0x78, 0xc2: 0x25, 0xc3: 0x2E, 0xc4: 0x1C, 0xc5: 0xA6, 0xc6: 0xB4, 0xc7: 0xC6, 0xc8: 0xE8,
    0xc9: 0xDD, 0xca: 0x74, 0xcb: 0x1F, 0xcc: 0x4B, 0xcd: 0xBD, 0xce: 0x8B, 0xcf: 0x8A,
    0xd0: 0x70, 0xd1: 0x3E, 0xd2: 0xB5, 0xd3: 0x66, 0xd4: 0x48, 0xd5: 0x03, 0xd6: 0xF6, 0xd7: 0x0E, 0xd8: 0x61,
    0xd9: 0x35, 0xda: 0x57, 0xdb: 0xB9, 0xdc: 0x86, 0xdd: 0xC1, 0xde: 0x1D, 0xdf: 0x9E,
    0xe0: 0xE1, 0xe1: 0xF8, 0xe2: 0x98, 0xe3: 0x11, 0xe4: 0x69, 0xe5: 0xD9, 0xe6: 0x8E, 0xe7: 0x94, 0xe8: 0x9B,
    0xe9: 0x1E, 0xea: 0x87, 0xeb: 0xE9, 0xec: 0xCE, 0xed: 0x55, 0xee: 0x28, 0xef: 0xDF,
    0xf0: 0x8C, 0xf1: 0xA1, 0xf2: 0x89, 0xf3: 0x0D, 0xf4: 0xBF, 0xf5: 0xE6, 0xf6: 0x42, 0xf7: 0x68, 0xf8: 0x41,
    0xf9: 0x99, 0xfa: 0x2D, 0xfb: 0x0F, 0xfc: 0xB0, 0xfd: 0x54, 0xfe: 0xBB, 0xff: 0x16
}


def subBytes(state):
    listSub = [Sbox[x] for x in state.flatten()]
    npSub = np.asarray(listSub)
    sBytes = (np.reshape(npSub, (4, 4)))

    return sBytes


def shiftRows(state):
    state[1] = np.roll(state[1], -1)
    state[2] = np.roll(state[2], -2)
    state[3] = np.roll(state[3], -3)

    shiftRows = state.copy()

    return shiftRows


def mixColumns(w):
    return polyMul(w[0], 2) ^ polyMul(w[1], 3) ^ polyMul(w[2], 1) ^ polyMul(w[3], 1), \
           polyMul(w[0], 1) ^ polyMul(w[1], 2) ^ polyMul(w[2], 3) ^ polyMul(w[3], 1), \
           polyMul(w[0], 1) ^ polyMul(w[1], 1) ^ polyMul(w[2], 2) ^ polyMul(w[3], 3), \
           polyMul(w[0], 3) ^ polyMul(w[1], 1) ^ polyMul(w[2], 1) ^ polyMul(w[3], 2)


def polyMul(x, y):
    if y == 1:
        return x
    tmp = (x << 1) & 0xff  # if theres a x**8 its gone cause of AND bitwise 1111 1111
    if y == 2:
        return tmp if x < 128 else tmp ^ 0x1b  # if the og was less than 128 than a shift to the left wouldnt have made it > GF(2**8)
    if y == 3:
        return polyMul(x, 2) ^ x  # poly (x+1)


# print(shiftRows(subBytes(startRound)))

#words = [(shiftRows(subBytes(startRound)).T[x]) for x in range(4)]

#mixcolmap = map(mixColumns, words)
#mixcol = list(mixcolmap)
# print(mixcol)
#mixcolArr = np.asarray(mixcol)
#mixCol = (np.reshape(mixcolArr, (4, 4))).T
#print("after mix columns\n")
#print(mixCol)


def keyExpansion(key, rcval):
    ckey = [key.T[x] for x in range(4)]
    w0 = ckey[0]
    w1 = ckey[1]
    w2 = ckey[2]
    w3 = ckey[3]

    w3sh = np.roll(w3, -1)

    w3sub = [Sbox[x] for x in w3sh]

    #print(w0,w1,w2,w3,w3sub)

    Rcon = np.array([[0x01, 0x00, 0x00, 0x00],
                     [0x02, 0x00, 0x00, 0x00],
                     [0x04, 0x00, 0x00, 0x00],
                     [0x08, 0x00, 0x00, 0x00],
                     [0x10, 0x00, 0x00, 0x00],
                     [0x20, 0x00, 0x00, 0x00],
                     [0x40, 0x00, 0x00, 0x00],
                     [0x80, 0x00, 0x00, 0x00],
                     [0x1B, 0x00, 0x00, 0x00],
                     [0x36, 0x00, 0x00, 0x00]]
                    )
    afterxorRcon = w3sub ^ Rcon[rcval]

    t0 = afterxorRcon ^ w0
    t1 = t0 ^ w1
    t2 = t1 ^ w2
    t3 = t2 ^ w3
    #print(afterxorRcon, t0, t1, t2, t3)
    roundKey = np.array([t0, t1, t2, t3]).T

    return roundKey

#roundKey = keyExpansion(keyArr, 0)
#print(roundKey)
#newround = np.bitwise_xor(roundKey, mixCol)
#print(newround)

def main(state):
    #aes start
    rcval = 0
    for x in range(9):
        subb = subBytes(state)
        #print(subb)
        shrows = shiftRows(subb)
        #print(shrows)

        #MIXCOLUMNS STUFF
        words = [(shrows.T[w]) for w in range(4)]
        mcmap = map(mixColumns, words)
        mixcolist = list(mcmap)

        mixcol = (np.reshape(np.asarray(mixcolist), (4, 4))).T
        #print(mixcol)

        if x == 0:
            roundKey = keyExpansion(keyArr, x)
            #print(roundKey)
        else:
            roundKey = keyExpansion(roundKey, x)
            #print(roundKey)

        state = np.bitwise_xor(roundKey, mixcol)
        #print(state)
        print(f"round{x+1} done")

    subb = subBytes(state)
    # print(subb)
    shrows = shiftRows(subb)
    roundKey = keyExpansion(roundKey, x+1)
    state = np.bitwise_xor(roundKey, shrows)
    print(f"round{x + 2} done")
    return state

print(main(startRound))
