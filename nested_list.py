if __name__ == '__main__':
    students = []
    marks = []
    for i  in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        if score not in marks:
            marks.append(score)
students.sort(key=lambda x: (x[1],x[0]))
marks.sort()
marks.pop(0)
sec_low = marks[0]
for x in students:
    if x[1] == sec_low:
        print(x[0])