input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum = 0 # 0으로 설정했기 때문에 여기도 고려해야 함 
    for num in array:
        if num <= 1 or multiply_sum <= 1:
            multiply_sum += num
        else:
            multiply_sum *= num
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)
