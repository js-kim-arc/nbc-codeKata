def solution(n):
    answer = []

    def hanoi(n, start, to, via):
        if n == 1:
            answer.append([start, to])
            return
        hanoi(n - 1, start, via, to)
        answer.append([start, to])
        hanoi(n - 1, via, to, start)

    hanoi(n, 1, 3, 2)
    return answer