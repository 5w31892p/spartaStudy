array = [5, 3, 2, 1, 6, 8, 7, 4]

# [5] [3] -> [3, 5]
# [2] [1] -> [1, 2]
# [6] [8] -> [6, 8]
# [7] [4] -> [4, 7]
# 다시
# [3, 5] [1, 2] -> [1, 2, 3, 5]
# [6, 8] [4, 7] -> [4, 6, 7, 8]
# 또 다시
# [1, 2, 3, 5] [4, 6, 7, 8] -> [1, 2, 3, 4, 5, 6, 7, 8]
#
# 1단계
# [1, 2, 3, 4, 5, 6, 7, 8] 길이 N
# [1, 2, 3, 5] [4, 6, 7, 8] 길이 N/2 2개 비교하며 병합
# -> N/2 * 2 = N
#
# 2단계
# [3, 5] [1, 2] -> [1, 2, 3, 5] 길이 N/4 2개 비교하며 병합
# [6, 8] [4, 7] -> [4, 6, 7, 8] 길이 N/4 2개 비교하며 병합
# -> N/4 * 4 = N
#
# K단계
# [1][5]...  -> 탈출조건 : 길이가 1일 때 슝
# K단계를 거치면 N의 길이였던 것이 반씩 반씩 반씩 쪼개서 1이 된다는 소리
# N /2^K = 1 -> K =log2N
# 즉, k단계 만큼 반복하되 각 단게는 O(N)만큼의 시간 복잡도를 가짐
# 즉, log2N * O(N) -> O(NlogN)



def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    lett_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    print(array)
    print('lett_array', lett_array)
    print('right_array', right_array)
    return merge(lett_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!



