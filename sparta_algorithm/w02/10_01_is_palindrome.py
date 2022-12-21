input = "abcba"


def is_palindrome(string):
    n = len(string)  # 문자열 길이 저장
    for i in range(n):
        if string[i] != string[n - 1 - i]:  # 문자열 맨 앞과 뒤가 같은지 비교
            return False

    return True


print(is_palindrome(input))
