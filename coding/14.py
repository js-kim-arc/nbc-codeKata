from functools import cmp_to_key


def solution(numbers):
    # 숫자를 문자열로 변환
    nums = list(map(str, numbers))

    def compare(a, b):
        if a + b > b + a:
            return -1  # a가 앞으로
        elif a + b < b + a:
            return 1  # b가 앞으로
        else:
            return 0

    nums.sort(key=cmp_to_key(compare))

    # 모두 0인 경우 "000..."이 아닌 "0"을 반환해야 함
    result = ''.join(nums)
    if result[0] == '0':
        return '0'
    return result