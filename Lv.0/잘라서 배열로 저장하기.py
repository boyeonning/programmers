def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]
        


my_str	= "abc1Addfggg4556b"	
n = 6

print(solution(my_str, n))