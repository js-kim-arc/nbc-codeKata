from collections import Counter


def solution(want, number, discount):
    wants = Counter(dict(zip(want, number)))
    window = Counter(discount[:10])

    answer = 0
    if all(window[item] >= cnt for item, cnt in wants.items()):
        answer += 1

    for i in range(10, len(discount)):
        window[discount[i]] += 1

        window[discount[i - 10]] -= 1

        if all(window[item] >= cnt for item, cnt in wants.items()):
            answer += 1

    return answer