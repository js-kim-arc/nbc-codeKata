def solution(n, m, section):
    answer = 0
    painted_end = 0

    for s in section:
        if s > painted_end:
            answer += 1
            painted_end = s + m - 1

    return answer