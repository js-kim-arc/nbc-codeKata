def solution(s, skip, index):
    alphabet = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in skip]
    pos = {c: i for i, c in enumerate(alphabet)}
    n = len(alphabet)
    return "".join(alphabet[(pos[c] + index) % n] for c in s)