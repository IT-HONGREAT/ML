# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,
# 시험은 최대 10,000 문제로 구성되어있습니다.
def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_one = 0
    count_two = 0
    count_three = 0

    rank = [0]

    while len(one) < len(answers):
        one += one
    while len(two) < len(answers):
        two += two
    while len(three) < len(answers):
        three += three

    i = 0
    while i < len(answers):
        if one[i] == answers[i]:
            count_one += 1

    # for i in range(len(answers)):
    #     if one[i] == answers[i]:
    #         count_one += 1
    # for i in range(len(two)):
    #     if two[i] == answer[i]:
    #         count_two += 1
    # for i in range(len(answers)):
    #     if three[i] == answer[i]:
    #         count_three += 1

    rank.append(count_one)
    rank.append(count_two)
    rank.append(count_three)

    first = max(rank)
    first_loc = rank.index(first)

    return int(first_loc)

print(solution([1,2,3,4,5]))