def solution(my_string, overwrite_string, s):
    answer = ''
    
    x = len(overwrite_string)
    my_string = my_string[ :s] + overwrite_string + my_string[s+x:]
    answer = my_string
    return answer