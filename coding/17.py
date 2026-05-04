def solution(sizes):
    normalized = [(max(w, h), min(w, h)) for w, h in sizes]

    max_width = max(w for w, _ in normalized)
    max_height = max(h for _, h in normalized)

    return max_width * max_height