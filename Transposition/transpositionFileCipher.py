import os, sys, time, Transposition.transpositionEncrypt as ENC, \
    Transposition.transpositionDecrypt as DEC


def main():
    f_key = 10
    # f_mode = 'encrypt'
    f_mode = 'decrypt'
    if f_mode == 'decrypt':
        input_filename = 'frankenstein.encrypt.txt'
    else:
        input_filename = 'frankenstein.txt'

    output_filename = f'frankenstein.{f_mode}.txt'

    if not os.path.exists(input_filename):
        print(f'File {input_filename} not exist, Quitting...')
        sys.exit()

    if os.path.exists(output_filename):
        print(
            f'File {output_filename} existed, will be overwrite. (C)ontinue or (Q)uit?')
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    # read file
    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()
    print(f'{f_mode.title()}ing...')

    start_time = time.time()
    if f_mode == 'encrypt':
        transformed = ENC.encrypt_msg(f_key, content)
    else:
        transformed = DEC.decrypt_msg(f_key, content)

    total_time = round(time.time() - start_time, 2)
    print(f'{f_mode.title()}sion tookes {total_time} seconds.')

    # write to file
    output_file_obj = open(output_filename, 'w')
    output_file_obj.write(transformed)
    output_file_obj.close()

    print(f'{output_filename} with {len(content)} {f_mode}ed done.')


if __name__ == '__main__':
    main()
