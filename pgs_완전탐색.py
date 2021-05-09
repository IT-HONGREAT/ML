def solution(answers):

    one = [1,2,3,4,5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    count_one = 0
    count_two = 0
    count_three = 0

    for i in range(0,len(answers)):
        if one[i] == answers[i]:
            count_one += 1
        if two[i] == answers[i]:
            count_two += 1
        if three[i] == answers[i]:
            count_three += 1

    rank = [0, count_one, count_two, count_three]

    temp = max(rank) 
    answer = []
    for i in range(len(rank)):
        if rank[i] == temp:
            answer.append(i)

    return answer
