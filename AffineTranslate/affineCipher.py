# affine encrypt 仿射加密: 乘数加密+凯撒移位
# 条件 gcd(key乘, len(符号集)) = 1 否则出现same mapping
# LINK: http://inventwithpython.com/hacking/chapter15.html
import sys

sys.path.append('..')
import cryptomath as mathutil

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main():
    msg = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    key = 2023
    mode = 'encrypt'

    if mode == 'encrypt':
        translated = encrypt_msg(key, msg)
    else:
        translated = decrypt_msg(key, msg)

    print(f"""mode: {mode.title()}, key: {key}
          \n origin msg: {msg}
          \n translated msg: {translated}""")

    print(f""" translated msg: {decrypt_msg(key, translated)}""")


def gen_keys(key):
    key_a = key // len(SYMBOLS)
    key_b = key % len(SYMBOLS)
    return key_a, key_b


def check_keys(key_a, key_b, mode):
    if mode == 'encrypt':
        if key_a == 1:
            sys.exit('key A == 1, change it')
        if key_b == 0:
            sys.exit('key B == 0, change it')
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        sys.exit('Requirement: key A，B > 0 && key_b < len')
    if mathutil.gcd(key_a, len(SYMBOLS)) != 1:
        sys.exit('Error: 乘法映射key和len不互素')
    return True


# key: type Number
# msg: type characters
def encrypt_msg(key, msg):
    key_a, key_b = gen_keys(key)
    check_keys(key_a, key_b, len(SYMBOLS))
    cipher_text = ''
    # letter
    for l in msg:
        if l in SYMBOLS:
            p_index = SYMBOLS.find(l)
            cipher_text += SYMBOLS[(p_index * key_a + key_b) % len(SYMBOLS)]
        else:
            cipher_text += l
    return cipher_text


def decrypt_msg(key, msg):
    key_a, key_b = gen_keys(key)
    plain_text = ''
    key_a_inv = mathutil.get_mod_inverse(key_a, len(SYMBOLS))
    for l in msg:
        if l in SYMBOLS:
            c_index = SYMBOLS.find(l)
            plain_text += SYMBOLS[
                ((c_index - key_b) * key_a_inv) % len(SYMBOLS)]
        else:
            plain_text += l

    return plain_text


if __name__ == '__main__':
    main()
