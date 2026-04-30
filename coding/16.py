import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)] # 이거 리팩토링 꼭 기억하기 - math 라이브러리 잘 쓰기

    count = 1
    current = days[0]

    for d in days[1:]:
        if d <= current:
            count += 1
        else:
            answer.append(count)
            current = d
            count = 1

    answer.append(count)  # 마지막 묶음
    return answer