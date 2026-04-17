def solution(players, callings):
    idx= {name:i for i, name in enumerate(players)}

    for name in callings:
        i=idx[name]
        front= players[i-1]

        players[i-1],players[i]=players[i],players[i-1]

        idx[name]=i-1
        idx[front]=i

    return players