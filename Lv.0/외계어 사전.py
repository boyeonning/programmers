def solution(spell, dic):
    spell = sorted(spell)
    dic  = [sorted(i) for i in dic]
    return 1 if spell in dic else 2

spell = ["p", "o", "s"]
dic = 	["sod", "eocd", "qixm", "adio", "soo"]

print(solution(spell, dic))