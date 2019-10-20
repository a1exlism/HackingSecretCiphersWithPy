import sys


def load_dictionary():
    # load English dictionary alpha means all letters
    w_obj = open('words_alpha.txt')
    dict_eng = {}
    for word in w_obj.read().split('\n'):
        dict_eng[word] = None
    w_obj.close()
    return dict_eng


def transform_letter(msg):
    UPPER_LATTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTER_SPACE = UPPER_LATTER + UPPER_LATTER.lower() + ' \t\n'

    new_msg = ''
    for c in msg:
        if c in LETTER_SPACE:
            new_msg += c
    return new_msg


# @type msg: string
def is_english(msg, std_word_precentage=20, std_letter_percentage=85):
    possible_words_list = msg.split()
    possible_counter = len(possible_words_list)
    # No msg
    if not possible_counter:
        return 0
    # with all letters
    ENGLISH_WORDS = load_dictionary()

    # count english words
    word_counter = 0
    for word in possible_words_list:
        if word in ENGLISH_WORDS:
            word_counter += 1

    # remove non letter
    msg_letter = transform_letter(msg)

    # precent for Python2.x

    msg_word_precentage = word_counter / possible_counter * 100
    msg_letter_precentage = float(len(msg_letter)) / len(msg) * 100

    # print(msg_word_precentage)
    # print(msg_letter_precentage)
    return msg_word_precentage >= std_word_precentage \
           and msg_letter_precentage >= std_letter_percentage
