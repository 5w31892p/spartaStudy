input = [4, 6, 2, 9, 1]


# 1번째 : [4, 6, 2, 9, 1] ←  6,4 비교
# 2번째 : [4, 6, 2, 9, 1] ← ←  2,6 / 2,4 비교
# 3번째 : [2, 4, 6, 9, 1] ← ← ←  9,6 비교 (제일 마지막보다 크기 때문에 한번만 비교)
# 4번째 : [2, 4, 6, 9, 1] ← ← ← ←  1,9 / 1,6 / 1,4 / 1,2 비교

# for i in range(1,5):
#     # 여기서 왜 range(5) 가 아니라 range(1, 5)인 이유는?
#     # 0 번째 인덱스는 이미 정렬된 상태라고 판단
#     # ∴ 1번째 인덱스부터 시작하겠다는 의미
#     for j in range(i):
#         # i가 늘어날 때마다  j 내부에 잇는 반복 횟수가 똑같이 증가하기 때문
#         print(i - j)


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
