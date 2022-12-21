input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array: # array 길이 만큼 아래 연산 실행
        for compare_num in array: # array 길이 만큼 아래 연산 실행
            if num < compare_num: # 비교 연산 1번 실행
                break
        else:
            return num


result = find_max_num(input)
print(result)

