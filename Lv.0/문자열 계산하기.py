def solution_1(my_string):
    my_string = my_string.split(' ')
    answer = int(my_string[0])
    for i in range(len(my_string)):
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        elif my_string[i] == '-':
            answer -= int(my_string[i+1])
    return answer

def solution_2(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

my_string = "3 + 4"
print(solution_1(my_string))