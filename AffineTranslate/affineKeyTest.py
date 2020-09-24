# Question: 仿射加密法可以有多少个密钥
import sys

sys.path.append('..')
import affineCipher, cryptomath

message = 'Make things as simple as possible, but not simpler.'
key_B = 1
# key_A - 乘法
for key_A in range(2, 100):
    key = key_A * len(affineCipher.SYMBOLS) + key_B
    if cryptomath.gcd(key_A, len(affineCipher.SYMBOLS)) == 1:
        print(key_A, affineCipher.encrypt_msg(key, message))

