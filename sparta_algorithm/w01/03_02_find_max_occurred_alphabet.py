input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26 # 26개 공간
    for char in string: #string 길이만큼 아래 연산 실행
        if not char.isalpha(): # 비교 연산 1번 실행
            continue # 코드실행 건너뛰기
        arr_index = ord(char) - ord("a") # 1개 공간 # 대입 연산 1번 실행 # 97-97
        alphabet_occurrence_array[arr_index] += 1 # 대입 연산 1번 실행

    max_occurrence = 0 # 1개 공간 # 대입 연산 1번 실행
    max_alphabet_index = 0 # 1개 공간 # 대입 연산 1번 실행
    for index in range(len(alphabet_occurrence_array)): # alphabet_array 의 길이(26)만큼 아래 연산이 실행
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index] # 1개 공간 # 대입 연산 1번 실행

        if alphabet_occurrence > max_occurrence: # 비교 연산 1번 실행
            max_alphabet_index = index # 대입 연산 1번 실행
            max_occurrence = alphabet_occurrence # 대입 연산 1번 실행
    print(max_alphabet_index)
    return chr(max_alphabet_index + ord("a"))

result = find_max_occurred_alphabet(input)
print(result)