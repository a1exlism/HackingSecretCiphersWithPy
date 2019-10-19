import random, sys, Transposition.transpositionEncrypt as E, \
    Transposition.transpositionDecrypt as D


def main():
    random.seed(42)

    for i in range(20):
        # random length
        msg = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        # msg = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        msg = list(msg)
        # shuffle
        random.shuffle(list(msg))
        msg = ''.join(msg)

        print(f'#{i} Origin: {msg}')
        for key in range(1, len(msg)):
            encrypted = E.encrypt_msg(key, msg)
            decrypted = D.decrypt_msg(key, encrypted)
            if msg != decrypted:
                print(f'Mismatch with key {key} and msg {msg}')
                print('encrypted: ' + encrypted)
                print('decrypted: ' + decrypted)
                sys.exit()
    print('Transposition cipher all passed')


if __name__ == '__main__':
    main()
