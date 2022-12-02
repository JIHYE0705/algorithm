def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # for word in string:
    #     if word.isalpha():
    #         ascii_num = ord(word) - ord('a')
    #         alphabet_occurrence_array[ascii_num] += 1
    #

    # 선생님 답
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
