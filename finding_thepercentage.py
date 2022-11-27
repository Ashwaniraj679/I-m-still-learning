if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks_specific = student_marks[query_name]
    avg = sum(marks_specific)/len(marks_specific)
    print('%.2f' % avg)