input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
            # 알파벳으로 전환해야하기 때문에 index 그대로 넣으면 안됨
    print(not_repeating_character_array) # 여기서 하면 알파벳 순서대로 c와 d가 모두 다 나옴

    for char in string: # 알파벳 순서가 아닌 들어온 문자열 순서에 맞게 반환
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_character(input)
print(result)
