from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    order = 0
    while q:
        idx, pri = q.popleft()
        if any(pri < other for _, other in q):   # 나보다 높은 게 남아있다면
            q.append((idx, pri))
        else:
            order += 1
            if idx == location:
                return order