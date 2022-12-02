input = "abcba"


def is_palindrome(string):
    for i in range(len((string)) // 2):
        if string[i] == string[-1 + i]:
            return True
        else:
            return False

    # 선생님 답답

    # n  len(string)
    # for i in range(n):
    #     if string[i] != string[n -1 - i]:
    #         return False
    # return True


print(is_palindrome(input))
