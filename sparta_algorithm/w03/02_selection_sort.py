input = [4, 6, 2, 9, 1]

# 1번째 : [4, 6, 2, 9, 1] // 4, 6, 2, 9, 1 중 최솟값 찾기!
# 2번째 : [1, 6, 2, 9, 4] // 6, 2, 9, 4 중 최솟값 찾기!
# 3번째 : [1, 2, 6, 9, 4] // 6, 9, 4 중 최솟값 찾기!
# 4번째 : [1, 2, 4, 9, 6] // 9, 6 중 최솟값 찾기!


# for i in range(5 - 1):
#     # Q. 여기서 왜 5 - 1 인 이유는?
#     for j in range(5 - i):
#         # A. 맨 마지막 비교는 하지 않아도 되기 때문
#         print(i + j)
#         # 위의 예시에서 4번째 비교를 하면 [1, 2, 4, 6, 9] 로 변경이 되는데,
#         # 굳이 9와 9를 비교할 필요가 없기 때문
#         # 앞에 다 최솟값이 갔으니 알아서 잘 가 있겠지? 하는 느낌


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i # 최소값 저장
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
