input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    # 각 문자열 비교를 위해
    # 26개 공간 사용
    max_occurrence = 0 # 최고로 많이 나온 횟수를 저장하는 변수
    # 1개 공간 사용
    max_alphabet = alphabet_array[0] # 최고로 많이 나온 알파벳 저장하는 변수
    # 1개 공간 사용

    for alphabet in alphabet_array: # alphabet_array의 길이(26)만큼 연산 실행
        occurrence = 0 # 1개 공간 사용 #대입 연산 1번 실행
        for char in string: #string  길이만큼 아래 연산 실행
            if char == alphabet: # 비교연산 1번 실행
                occurrence += 1 # 대입 연산 1번 실행

        if occurrence > max_occurrence: # 비교 연산 1번 실행
            max_alphabet = alphabet # 대입 연산 1번 실행
            max_occurrence = occurrence # 대입 연산 1번 실행

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)