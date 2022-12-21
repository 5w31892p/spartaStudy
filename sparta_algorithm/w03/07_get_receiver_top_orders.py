top_heights = [6, 9, 5, 7, 4]

# [0, 0, 2, 2, 4]이 답인데 처음엔 # [0, 0, 0, 0, 0]으로 초기화

# 레이저 왼쪽방향
# 오른쪽부터 탐색
# 6  9  5  7  4
# [0, 0, 0, 0, 4]
# 6  9  5  7
# [0, 0, 0, 2, 4]
# 6  9  5
# [0, 0, 2, 2, 4]
# 6  9
# [0, 0, 2, 2, 4]
# 6
# [0, 0, 2, 2, 4]

# 끝에서부터 사라진다 == stack 자료구조

# for idx in range(5 - 1, 0, -1):
#     print(idx)
    # 5 - 1은 인덱스로 보니까 0~4이므로 5 -1 시작점
    # 0 끝나는 점
    # -1씩 줄어들면서 하겠다는 의미
# range란?
# range (시작점, 끝나는점, 어떻게 연산을 하나씩 줄여갈건가하는 설명)


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)  # [0, 0, 0, 0, 0]
    while heights:  # heights가 빈상태가 아닐 때까지
        height = heights.pop()  # heights 맨 뒤 뽑기
        # [6, 9, 5, 7]
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                # 인덱스가 아닌 위치를 알려줘야 하므로 + 1
                # 스택에서 하나를 뺀 다음 하나의 인덱스를 알기 위해서는 현재 나와있는 스택의 길이가 인덱스!!
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
