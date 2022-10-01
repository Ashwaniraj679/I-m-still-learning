if __name__ == '__main__':
    students = []
    for i  in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
students.sort(key=lambda x: (x[1],x[0]))
for x in students:
    if students[1][1] == x[1]:
        print(x[0])
