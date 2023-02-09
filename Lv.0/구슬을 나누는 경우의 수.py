
def solution(balls, share):
    def factorial(num):
        sum=1
        for i in range(1, num+1):
            sum*=i
        return sum

    return factorial(balls) / (factorial(balls - share) * factorial(share))

balls = 3
share = 2
print(solution(balls, share))

# 서로 다른 n개 중 m개를 뽑는 경우의 수 공식은 다음과 같습니다.
# n! / (n-m)! x m!
