# https://school.programmers.co.kr/learn/courses/30/lessons/120884

chicken	= 100

def solution1(chicken):
    service = chicken // 10
    coupon = service + (chicken % 10)

    while coupon >= 10:
        service += coupon // 10
        coupon = (coupon // 10) + (coupon%10)  # divmod 사용
    return service

print(solution1(chicken))