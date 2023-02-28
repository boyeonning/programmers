# https://school.programmers.co.kr/learn/courses/30/lessons/120878

a = 7
b = 20

def solution(a, b):
    if a % b == 0:
        return 1 
    else:

        dividor = [i for i in range(1, min(a,b)+1) if a % i == 0 and b % i == 0][-1]
        
        b = b // dividor

        for x in range(2, b+1):
            if b % x == 0 and x ==2 or x == 5:
                return 1
            return 2 

print(solution(a, b))
