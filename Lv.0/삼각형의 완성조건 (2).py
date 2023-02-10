
def solution_1(sides):
    total = []
    sides = sorted(sides)

    x = sides[-1] - sides[0]
    for i in range(x+1, sides[-1]+1):
        total.append(i)

    for j in range(sides[-1]+1, sum(sides)):
        total.append(j)

    return len(total)

def solution_2(sides):
    # 1.최대 길이의 변이 없는 경우
    # x < sum(sides)

    # 2. 최대 길이의 변이 존재 
    # max(sides) < min(sides) + x

    #위의 두 식 합치면
    # (max(sides) - min(sides)) < x < sum(sides)
    return sum(sides) - (max(sides) - min(sides)) -1

sides = [3, 6]	
print(solution_2(sides))
