def solution(numbers):
    list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in list:
        numbers = numbers.replace(i, str(list.index(i)))
    return int(numbers)


numbers	= "onefourzerosixseven"	
print(solution(numbers))