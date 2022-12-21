input = 20


def find_prime_list_under_number(number):
    num = []
    for a in range(2, number + 1): # n까지 포함하기 위해 ; range 범위의 특성
        for b in num:
            if a % b == 0 and b * b <= a:
                break
        else:
            num.append(a)

    return num


result = find_prime_list_under_number(input)
print(result)
