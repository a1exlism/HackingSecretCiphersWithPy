# @description detect a message is English
def is_english(msg, percent_word=20, percent_letter=85):
    UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
    # 0. init msg to upper letters
    msg = msg.upper()
    # 1. load basic English dictionary
    en_dict = {}
    dict_file = open('dictionary.txt')
    for word in dict_file.read().split('\n'):
        en_dict[word] = None
    dict_file.close()
    # 2. generate pure letter from msg and get letter counts
    msg_letter = ''
    for c in msg:
        if c in LETTERS_AND_SPACE:
            msg_letter += c
    # split all space( \t\n)
    msg_possible_words = msg_letter.split()
    # msg_letter = ''.join(msg_possible_words)
    count_letter = len(msg_letter)
    if count_letter == 0:
        return False

    # print(f"""msg_letter: {msg_letter}""")
    # print(f"""msg_letter_arr: {msg_possible_words}""")

    # 3. get possible english words count
    count_en = 0
    for word in msg_possible_words:
        if word in en_dict:
            count_en += 1
    # 4. calculate the percent EN words/all letters and return result
    # percent of english words in all words
    percent_word_now = count_en / len(msg_possible_words) * 100
    # percent of letters in all characters
    percent_letter_now = float(count_letter) / len(msg) * 100

    # print(percent_word_now)
    # print(percent_letter_now)

    return percent_word_now >= percent_word and percent_letter_now >= percent_letter
