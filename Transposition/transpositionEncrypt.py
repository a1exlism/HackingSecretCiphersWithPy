def main():
    # plain_text = 'ABCDEF GHI JKLM NOPQRSTUV WXYZ'
    plain_text = 'Common sense is not so common.'
    key = 8
    print(encrypt_msg(key, plain_text))


def encrypt_msg(key, msg):
    # with slice
    arr_list = []
    i = 0
    cipher = ''
    while i < key:
        # print(msg[i::key])
        cipher += msg[i::key]
        i += 1
    # print(cipher)
    return cipher


if __name__ == '__main__':
    main()
