def solution(s):
    sum =0
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] == 'Z':
            sum -= int(s[i-1])
        else:
            sum+=int(s[i])
    return sum

s = "10 20 30 40"

print(solution(s))

