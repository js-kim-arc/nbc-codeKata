from bisect import bisect_left

def solution(citations):
    citations = sorted(citations)  # 오름차순 정렬
    n = len(citations)
    left, right = 0, n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        idx = bisect_left(citations, mid)
        count = n - idx

        if count >= mid:
            # 조건 만족 → 더 큰 h 시도
            answer = mid
            left = mid + 1
        else:
            # 조건 불만족 → h를 줄여야 함
            right = mid - 1

    return answer