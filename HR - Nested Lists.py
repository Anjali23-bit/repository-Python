from operator import itemgetter
if __name__ == '__main__':
    students=[]
    lowest_score=0;
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    min1 = min(students, key=itemgetter(1))[1]
    rem_min= [i for i in students if i[1] != min1]
    min2= min(rem_min,key=itemgetter(1))[1]
    final_list= [i[0] for i in rem_min if i[1] == min2]
    final_list.sort()
    for i in final_list:
        print(i)