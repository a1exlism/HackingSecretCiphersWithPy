import sys, Transposition.BruteForce.detectEnglish as detectEN, \
    Transposition.transpositionDecrypt as DEC


def main():
    # file ops
    f_obj = open('frankenstein.encrypt.txt')
    encrypted_msg = f_obj.read()
    f_obj.close()
    # try decrypt
    for key in range(1, len(encrypted_msg)):
        plain_msg = DEC.decrypt_msg(key, encrypted_msg)
        if detectEN.is_english(plain_msg, 35):
            print(f'Possible solution key: {key}')
            print(f'100th words: {plain_msg[:100]}')
            print('(C)ontinue or (Q)uit')
            flag = input('> ')
            if not flag.lower().startswith('c'):
                out_obj = open('decrypted.txt', 'w')
                out_obj.write(plain_msg)
                out_obj.close()
                sys.exit()


if __name__ == '__main__':
    main()
