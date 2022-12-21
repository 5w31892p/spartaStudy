input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max_num = array[0] # 임의숫자 넣으면서 갈 것이기 때문에 초기값 설정해주는 것
    # 연산 1번 실행
    for num in array: # array의 길이만큼 아래 연산 실행
        if num > max_num: # 비교 연산 1번 실행
            max_num = num # 대입 연산 1번 실행

    return max_num


result = find_max_num(input)
print(result)
