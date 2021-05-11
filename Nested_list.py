#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#if there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    name_score = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pair = list((name, score))
        name_score.append(pair)
        score_list.append(score)
        
    second_lowest = sorted(list(set(score_list)))
    name_score.sort()
    for inner in name_score:
        if inner [1] == second_lowest[1]:
            print (inner[0])
        
