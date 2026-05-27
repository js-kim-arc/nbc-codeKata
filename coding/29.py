def solution(order):
    n = len(order)
    stack = []
    belt = 1
    idx = 0
    loaded = 0

    while idx < n:
        need = order[idx]

        if stack and stack[-1] == need:
            stack.pop()
            loaded += 1
            idx += 1
        elif belt <= n:
            if belt == need:
                loaded += 1
                idx += 1
            else:
                stack.append(belt)
            belt += 1
        else:
            break

    return loaded