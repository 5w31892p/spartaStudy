finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    a = 0
    b = len(numbers) - 1
    t = (a+b) // 2

    while a <= b:
        if numbers[t] == target:
            return True
        elif numbers[t] < target:
            a = t + 1
        else:
            b = t -1
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
