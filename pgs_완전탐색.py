def solution(answers):

    one = [1,2,3,4,5] * 250
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 111
    three  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 100

    rank = [0]
    #새로운 수포자들의 리스트와 정답을 비교해서 같은 숫자가 제일 많은 사람이 1등으로 하고, 그 1등을 rank리스트에 담자.
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

    rank.append(count_one)
    rank.append(count_two)
    rank.append(count_three)

    #rank리스트에 들어간 숫자는 수포자1,2,3의 정답개수이다. 정답 개수가 제일 높은 숫자를 찾고, 그에 해당하는 인덱스를 뽑아내자
    temp = max(rank) #제일 많이 맞춘 갯수를 찾기
    a = list(filter(lambda x: rank[x] == temp, range(len(rank)))) # 랭크리스트에서 최대값과 같은 값을 같는 리스트의 위치를 리스트로 만듬.

    return a

print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print(solution([2,3,4,5,1,1,1,2,3,2,2,1,2,3,2]))
print(solution([1,3,2,4,2,2,3,1,4,4,2,2,1,3,2,1,2,1,2,2,3,2,2,1,2,3,2,1,1,1,1]))
