import math


def main():
    # encrypt 和 decrypt 方式基本一致，实质上就是矩阵转置 Matrix Transpose
    # ATTENTION: 但是最后剩余空格>1时，需要注意横向-纵向问题，所以需要构造空格。
    enc = 'Cenoonommstmme oo snnio. s s c'
    # 这里假设split key已知(row)
    key = 8
    decrypt_msg(key, enc)


def decrypt_msg(key, enc):
    len_enc = len(enc)
    columns = math.ceil(len_enc / key)
    # 空余内容构造
    if len_enc % key != 0:
        remain_space_num = key - len_enc % key
    else:
        remain_space_num = 0
    if remain_space_num > 1:
        # string reverse
        enc_l = list(enc)
        # print(enc_l)
        i = columns * (key - remain_space_num) - 1
        # print('i: ' + str(i))
        while remain_space_num > 0:
            i += columns
            enc_l.insert(i, ' ')
            remain_space_num -= 1
        enc = ''.join(enc_l)
    # print(columns)
    dec = ''
    for i in range(columns):
        # print(i)
        # print(enc[i::columns])
        dec += enc[i::columns]

    return dec[:len_enc]
    # print(dec)


if __name__ == '__main__':
    main()
