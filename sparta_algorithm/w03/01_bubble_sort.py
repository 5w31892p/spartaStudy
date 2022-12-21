input = [4, 6, 2, 9, 1]

# 1번째 : [4, 6, 2, 9, 1]
#           →  →  →  →
# 2번째 : [4, 2, 6, 1, 9]
#           →  →  →
# 3번째 : [2, 4, 1, 6, 9]
#           →  →
# 4번째 : [2, 1, 4, 6, 9]
#           →

# for i in range(5 - 1):
    # 4번만 비교하면 되니까!
# for j in range(5 - i - 1):
    # Q. 여기서ㅓ왜 5 - i - 1 일까요?
# print(j)
    # A. array[j] 와 array[j + 1] 을 비교할거라,
    # 마지막 원소까지 가지 않아도 되기 때문


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
