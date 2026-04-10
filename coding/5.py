def solution(s):
    words = s.split(" ")

    answer = [
        "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))
        if word else ""  # 빈 문자열 처리 (다중 공백 사이)
        for word in words
    ]
    return " ".join(answer)

print(solution("try hello world"))
print(solution("try  hello"))