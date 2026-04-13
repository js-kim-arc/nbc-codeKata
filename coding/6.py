def solution(lottos, win_nums):
    win_set = set(win_nums)
    zeros = lottos.count(0)
    matched = sum(1 for n in lottos if n in win_set)

    def get_rank(cnt):
        return max(1, 7 - cnt) if cnt >= 2 else 6

    best = get_rank(matched + zeros)
    worst = get_rank(matched)

    return [best, worst]


lottos   = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))