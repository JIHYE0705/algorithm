s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    # count = 0
    # if count <= 0:
    #     return False
    # for i in range(len(string)):
    #     if string[i] == '(':
    #         count += 1
    #     elif string[i] == ')':
    #         count -= 1
    # if count == 0:
    #     return True
    #
    # return False

    #선생님 답
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!