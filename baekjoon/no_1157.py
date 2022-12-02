# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 딕셔너리 사용

# string = input().upper()
# word_dict = {}
# value = 0
#
# for word in string:
#     if word in word_dict:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = value + 1
#
# max_count = max(word_dict.values())
# max_word = []
#
# for key,value in word_dict.items():
#     if value == max_count:
#         max_word.append(key)
#
# if len(max_word) != 1:
#     print('?')
# else:
#     print(max_word.pop())


# Counter 내장함수 사용

from sys import stdin
from collections import Counter

word = stdin.readline().strip().upper()

most_word = Counter(word).most_common(2)

if len(most_word) >= 2:
    first_word = most_word[0]
    second_word = most_word[1]
    if first_word[1] == second_word[1]:
        print('?')
    else:
        print(first_word[0])
else:
    print(most_word[0][0])
