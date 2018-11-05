def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for index in range(len(completion)):
        if completion[index] != participant[index]:
            answer = participant[index]
            break
    return answer
