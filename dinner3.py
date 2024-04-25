def find_longest_word(word_list):
    longest_word = ""
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word, max_length

