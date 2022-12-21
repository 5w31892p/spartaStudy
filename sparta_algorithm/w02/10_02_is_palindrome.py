input = "소주만병만주소"


def is_palindrome(string):  # input값 들어감
    # 1. is_palindrome("소주만병만주소") True
    # 2. is_palindrome("주만병만주") True
    # 3. is_palindrome("만병만") True

    if string[0] != string[-1]:
        return False
        # 처음부터 틀렸을 때!
    if len(string) <= 1:
        return True # 4. is_palindrome("병")
        # 글자가 하나만 남았을 때!

    return is_palindrome(string[1:-1])
    # 첫번째 인덱스 ~ -1 인덱스 전까지
    # 첫번째로 본 인덱스 한칸 뒤 ~ - 뒤에서 한칸 앞 인덱스까지


print(is_palindrome(input))
