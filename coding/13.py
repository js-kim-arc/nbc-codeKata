def solution(ingredient):
    stack=[]
    answer = 0
    for x in ingredient:
        stack.append(x)
        if stack[-4:] == [1,2,3,1]:
            del stack[-4:]
            answer +=1
    return answer