def solution(n):
    pattern = "수박"

    answer = pattern * (n // 2)

    if n % 2 == 1:
        answer += "수"

    return answer