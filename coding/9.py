def solution(wallpaper):
    min_r, min_c = float('inf'), float('inf')
    max_r, max_c = float('-inf'), float('-inf')

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_r = min(min_r, i)
                min_c = min(min_c, j)
                max_r = max(max_r, i)
                max_c = max(max_c, j)

    return [min_r, min_c, max_r + 1, max_c + 1]