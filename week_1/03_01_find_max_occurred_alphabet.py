input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    # 알파벳의 빈도수 먼저 계산
    for word in string:
        if word.isalpha():
            index = ord(word)  - ord('a')
            alphabet_occurrence_array[index] += 1


    # 가장 많이 나온 알파벳 찾기
    max_alphabet = 0
    max_index_num = 0

    for index in range(len(alphabet_occurrence_array)):
        if max_alphabet < alphabet_occurrence_array[index]:
            max_alphabet = alphabet_occurrence_array[index]
            max_index_num = index

    answer = max_index_num + ord('a')
    return chr(answer)


    # 선생님 답
    # alphabet_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # max_occurrence = 0
    # max_alphabet = alphabet_array[0]
    #
    # for alphabet in alphabet_array:
    #     occurrence = 0
    #     for char in string:
    #         if char == alphabet:
    #             occurrence += 1
    #     if occurrence > max_occurrence:
    #         max_occurrence = occurrence
    #         max_alphabet = alphabet
    #
    # return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)