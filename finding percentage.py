#finding percentage of a cls upto 3 scores 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for names in student_marks:
        if(str(names)==query_name):
            a = sum(list(student_marks[names]))/3
            print('%.2f' %a)
            break
