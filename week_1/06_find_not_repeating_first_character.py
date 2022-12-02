input = "abacabade"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!

    # 알파벳이 몇번 나오는지 체크
    alphabet_occurrence_array = [0] * 26

    for word in string:
        if word.isalpha():
            index = ord(word) - ord('a')
            alphabet_occurrence_array[index] += 1

    # 한번만 나왔던 알파벳 체크
    not_repeating_word = []
    for i in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[i]
        if alphabet_occurrence == 1:
            not_repeating_word.append(chr(i + ord('a')))

    # 한번만 나온 알파벳들 중 먼저 나온 알파벳 리턴
    for word in string:
        if word in not_repeating_word:
            return word

    # 중복없는 알파벳이 없을 때 리턴해주는 값
    return '_'

    # 선생님 답
    # alphabet_occurrence_array = [0] * 26
    #
    # for char in string:
    #     if not char.isalpha():
    #         continue
    #     arr_index = ord(char) - ord('a')
    #     alphabet_occurrence_array[arr_index] += 1
    #
    # not_repeating_character_array = []
    # for index in range(len(alphabet_occurrence_array)):
    #     alphabet_occurrence = alphabet_occurrence_array[index]
    #     if alphabet_occurrence == 1:
    #         not_repeating_character_array.append(chr(index + ord('a')))
    #
    # for char in string:
    #     if char in not_repeating_character_array:
    #         return char
    #
    # return "_"


result = find_not_repeating_character(input)
print(result)
