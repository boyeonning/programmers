# https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution1(id_pw, db):
    if id_pw in db:
        return 'login'
    
    id = [x[0] for x in db]
    if id_pw[0] in id:
        return 'wrong pw'
    else:
        return 'fail'



id_pw = ["programmer01", "15789"]	
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

# print(solution1(id_pw, db))


def solution2(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

# print(solution2(id_pw, db))
# 변수 := 표현식
if db_pw := dict(db).get(id_pw[0]):
    if db_pw == id_pw[1]:
        print('login')
    else:
        print('wrong pw')
