# https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution1(dots):
    dots = sorted(dots)
    x = dots[-1][0] - dots[0][0]
    y = dots[-1][1] -  dots[0][1]
    return x*y

dots = [[-1, -1], [1, 1], [1, -1], [-1, 1]]	
print(solution1(dots))

def solution2(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
