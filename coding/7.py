def solution(today, terms, privacies):
    term_map = {}
    for term in terms:
        kind, months = term.split()
        term_map[kind] = int(months)

    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d

    today_days = to_days(today)
    result = []

    for i, privacy in enumerate(privacies):
        date, kind = privacy.split()
        expire_days = to_days(date) + term_map[kind] * 28

        if expire_days <= today_days:
            result.append(i + 1)

    return result