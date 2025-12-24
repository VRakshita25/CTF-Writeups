from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

# ciphertext from output.txt
with open("output.txt", "r") as f:
    cipher_hex = f.read().strip()

cipher_hex = "".join(cipher_hex.split())  # remove spaces/newlines
print("Hex length:", len(cipher_hex))
cipher = bytes.fromhex(cipher_hex)


# keystream generator
def p(s):
    x = s
    o = []
    for i in range(128):
        x = (x * 1103515245 + 12345 + i) & 0xffffffff
        o.append((x ^ (x >> 16)) & 0xff)
    return bytes(o)

# fake flag length is unknown, but AES padding tells us
# brute-force length is small (CTF flag)
for L in range(10, 50):
    for sm in range(1, 3000):
        s = ((sm << 3) ^ (L * 1337)) & 0xffffffff
        st = p(s)

        a = hashlib.sha256(st[:64]).digest()
        b = hashlib.sha256(st[64:] + a[:11]).digest()
        k = hashlib.sha256(b + a).digest()[:16]
        v = hashlib.md5(a).digest()

        try:
            pt = AES.new(k, AES.MODE_CBC, v).decrypt(cipher)
            pt = unpad(pt, 16)
        except:
            continue

        # reverse stage 2
        x = pt[::-1]
        x = bytearray(x)

        for i in range(len(x)):
            r = i % 6 + 1
            x[i] = ((x[i] >> r) | (x[i] << (8 - r))) & 0xff
            x[i] ^= st[(i * 9) % len(st)]

        try:
            flag = bytes(x)
            if flag.startswith(b"ShaZ{"):
                print(flag)
                exit()
        except:
            pass
