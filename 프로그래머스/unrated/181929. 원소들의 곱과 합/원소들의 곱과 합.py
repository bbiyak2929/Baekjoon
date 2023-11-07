def solution(num_list):
    answer = 1
    sam = 0
    for i in range(len(num_list)):
        answer = answer * (num_list[i])
        sam = sam + (num_list[i])
    
    if answer < sam **2:
        return 1
    else:
        return 0