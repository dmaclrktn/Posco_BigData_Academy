import sys

data = []

def show():

    print("Student \t Name\t     Midterm   Final  Average  Grade\t")
    print("---------------------------------------------------------")
    for k in range(len(data)):
        for l in range(len(data[k])):
            print(str(data[k][l]), end = "\t")
        print()


def search():
    com_id = input("Student ID: ")
    student_id = []
    for i in range(len(data)):
        student_id.append(data[i][0])

    if com_id in student_id:
        print("Student \t Name\t     Midterm   Final  Average  Grade\t")
        print("---------------------------------------------------------")
        for i in range(len(data[student_id.index(com_id)])):
            print(data[student_id.index(com_id)][i],end = "\t")
        print()
    else:
        print("NO SUCH PERSON")

def changescore():
    com = input("Student ID: ")
    student_id = []
    for i in range(len(data)):
        student_id.append(data[i][0])

    if com in student_id:
        m_f = input("Mid/Final? ")
        while True:
            if m_f == "Mid": # 중간 고사 점수 수정
                mid_score = input("Input new score: ")
                if mid_score.isdigit():
                    mid_score = int(mid_score)
                    if mid_score > 100:
                        print("0~100 사이값으로 재입력하세요")
                        continue
                    elif mid_score <0 :
                        print("0~100 사이값으로 재입력하세요")
                        continue
                    else:
                        print("Student \t Name\t     Midterm   Final  Average  Grade\t")
                        print("---------------------------------------------------------")
                        for i in range(len(data[student_id.index(com)])):
                            print(data[student_id.index(com)][i],end = "\t")
                        print("")
                        print("Score changed.")
                        data[student_id.index(com)][2] = mid_score
                        data[student_id.index(com)][4] = (mid_score + int(data[student_id.index(com)][3])) / 2
                        data[student_id.index(com)][4] = round(data[student_id.index(com)][4],1)
                        if data[student_id.index(com)][4] >= 90 :
                            data[student_id.index(com)][5] = "A"
                        elif data[student_id.index(com)][4] >= 80:
                            data[student_id.index(com)][5] = "B"
                        elif data[student_id.index(com)][4] >= 70:
                            data[student_id.index(com)][5] = "C"
                        elif data[student_id.index(com)][4] >= 60:
                            data[student_id.index(com)][5] = "D"
                        else:
                            data[student_id.index(com)][5] = "F"
                        for i in range(len(data[student_id.index(com)])):
                            print(data[student_id.index(com)][i],end = "\t")
                        data.sort(key = lambda a : a[4], reverse = True)
                        print()
                        break
                else:
                    print("0~100 사이값으로 재입력하세요")
                    continue

            elif m_f == "Final": # 기말고사 성적 입력
                final_score = input("Input new score: ")
                if final_score.isdigit():
                    final_score = int(final_score)
                    if final_score > 100:
                        print("0~100 사이값으로 재입력하세요")
                        continue
                    elif final_score <0 :
                        print("0~100 사이값으로 재입력하세요")
                        continue
                    else:
                        print("Student \t Name\t     Midterm   Final  Average  Grade\t")
                        print("---------------------------------------------------------")
                        for i in range(len(data[student_id.index(com)])):
                            print(data[student_id.index(com)][i],end = "\t")
                        print("")
                        print("Score changed.")
                        data[student_id.index(com)][3] = final_score
                        data[student_id.index(com)][4] = (final_score + int(data[student_id.index(com)][2])) / 2
                        data[student_id.index(com)][4] = round(data[student_id.index(com)][4],1)
                        if data[student_id.index(com)][4] >= 90 :
                            data[student_id.index(com)][5] = "A"
                        elif data[student_id.index(com)][4] >= 80:
                            data[student_id.index(com)][5] = "B"
                        elif data[student_id.index(com)][4] >= 70:
                            data[student_id.index(com)][5] = "C"
                        elif data[student_id.index(com)][4] >= 60:
                            data[student_id.index(com)][5] = "D"
                        else:
                            data[student_id.index(com)][5] = "F"
                        for i in range(len(data[student_id.index(com)])):
                            print(data[student_id.index(com)][i],end = "\t")
                        data.sort(key = lambda a : a[4], reverse = True)
                        print()
                        break
                else:
                    print("0~100 사이값으로 재입력하세요")
                    continue
            else:
                print("다시 입력해주세요 : ")
                break


    else:
        print("NO SUCH PERSON")


def add():
    com_add = input("Student ID: ")
    student_id = []
    for i in range(len(data)):
        student_id.append(data[i][0])

    if com_add in student_id:
        print("ALREADY EXISTS.")
    else:
        while True:
            new_stu = []
            new_name = input("Name: ")
            new_mid = input("Midterm Score: ")
            if new_mid.isdigit():
                new_mid = int(new_mid)
                if new_mid > 100:
                    print("점수는 0~100점 사이로 입력해주세요")
                    continue
                elif new_mid <0:
                    print("점수는 0~100점 사이로 입력해주세요")
                    continue
                else:
                    pass
            else:
                print("점수는 0~100점 사이로 입력해주세요")
                continue
            

            new_final = input("Final Score: ")
            if new_final.isdigit():
                new_final = int(new_final)
                if new_final > 100:
                    print("점수는 0~100점 사이로 입력해주세요")
                    continue
                elif new_final <0:
                    print("점수는 0~100점 사이로 입력해주세요")
                    continue
                else:
                    pass
            else:
                print("점수는 0~100점 사이로 입력해주세요")
                continue
                
            new_stu.append(com_add)
            new_stu.append(new_name)
            new_stu.append(new_mid)
            new_stu.append(new_final)
            new_sco = (new_mid+new_final)/2
            new_sco = round(new_sco,1)
            new_stu.append(new_sco)
            if new_sco >= 90:
                new_stu.append("A")
            elif new_sco >= 80:
                new_stu.append("B")
            elif new_sco >= 70:
                new_stu.append("C")
            elif new_sco >= 60:
                new_stu.append("D")
            else:
                new_stu.append("F")
            break
        print("Student added.")

        data.append(new_stu)


def searchgrade():
    com_gra = input("Grade to search : ")
    student_gra = []
    A_stu = []
    B_stu = []
    C_stu = []
    D_stu = []
    F_stu = []
    
    for i in range(len(data)):
        student_gra.append(data[i][4])
        
    for n in student_gra:
        if n >= 90:
            A_stu.append(data[student_gra.index(n)])
        elif n >= 80:
            B_stu.append(data[student_gra.index(n)])
        elif n >= 70:
            C_stu.append(data[student_gra.index(n)])
        elif n >= 60:
            D_stu.append(data[student_gra.index(n)])
        else:
            F_stu.append(data[student_gra.index(n)])
    
    if com_gra == "A":
        if len(A_stu) == 0:
            print("NO RESULTS")
        else:
            print("Student \t Name\t     Midterm   Final  Average  Grade\t")
            print("---------------------------------------------------------")
            for i in range(len(A_stu)):
                for j in range(len(A_stu[i])):
                    print(A_stu[i][j],end = "\t")
                print()
            

    elif com_gra == "B":
        if len(B_stu) == 0:
            print("NO RESULTS")
        else:
            print("Student \t Name\t     Midterm   Final  Average  Grade\t")
            print("---------------------------------------------------------")
            for i in range(len(B_stu)):
                for j in range(len(B_stu[i])):
                    print(B_stu[i][j],end = "\t")
                print()
            
        
    elif com_gra == "C":
        if len(C_stu) == 0:
            print("NO RESULTS")
        else:
            print("Student \t Name\t     Midterm   Final  Average  Grade\t")
            print("---------------------------------------------------------")
            for i in range(len(C_stu)):
                for j in range(len(C_stu[i])):
                    print(C_stu[i][j],end = "\t")
                print()
            


    elif com_gra == "D":
        if len(D_stu) == 0:
            print("NO RESULTS")
        else:
            print("Student \t Name\t     Midterm   Final  Average  Grade\t")
            print("---------------------------------------------------------")
            for i in range(len(D_stu)):
                for j in range(len(D_stu[i])):
                    print(D_stu[i][j],end = "\t")
                print()
            


    elif com_gra == "F":
        if len(F_stu) == 0:
            print("NO RESULTS")
        else:
            print("Student \t Name\t     Midterm   Final  Average  Grade\t")
            print("---------------------------------------------------------")
            for i in range(len(F_stu)):
                for j in range(len(F_stu[i])):
                    print(F_stu[i][j],end = "\t")
                print()
            

    else:
        print("A,B,C,D,F 중에 입력해주세요.")


def remove():
    com_rem = input("Student ID: ")
    student_id = []
    for i in range(len(data)):
        student_id.append(data[i][0])

    if com_rem in student_id:
        del data[student_id.index(com_rem)]
        print("Student removed")

    elif len(student_id) == 0:
        print("List is empty")
    else:
        print("NO SUCH PERSON")




def main():
    if len(sys.argv) == 1:
        file_name = "students.txt"
    else:
        file_name = sys.argv[1]
    with open(file_name, "r") as students_score:
        for i in students_score:
            data.append(i.replace("\n","").split("\t"))

        for j in range(len(data)):
            avg = (int(data[j][2]) + int(data[j][3].replace("\n","")))/2
            avg = round(avg,1)
            data[j].append(avg)
            if avg >= 90:
                data[j].append("A")
            elif avg >= 80:
                data[j].append("B")
            elif avg >= 70:
                data[j].append("C")
            elif avg >= 60:
                data[j].append("D")
            else:
                data[j].append("F")
        data.sort(key = lambda a : a[4], reverse = True)
        while True:
            command = input("#")
            command = command.lower()
            if command == "show":
                data.sort(key = lambda a : a[4], reverse = True)
                show()
            elif command == "search":
                data.sort(key = lambda a : a[4], reverse = True)
                search()
            elif command == "changescore":
                data.sort(key = lambda a : a[4], reverse = True)
                changescore()
            elif command == "add":
                data.sort(key = lambda a : a[4], reverse = True)
                add()
            elif command == "searchgrade":
                data.sort(key = lambda a : a[4], reverse = True)
                searchgrade()
            elif command == "remove":
                data.sort(key = lambda a : a[4], reverse = True)
                remove()
            elif command == "quit":
                data.sort(key = lambda a : a[4], reverse = True)
                com_rem = input("Save data? [yes/no]: ")
                if com_rem == "yes":
                    file_name = input("File name : ")
                    with open(file_name , "w") as new_file:
                        for i in range(len(data)):
                            for j in range(4):
                                new_file.write(str(data[i][j]))
                                new_file.write("\t")
                            new_file.write("\n")
                    break

                elif com_rem == "no":
                    break

                else:
                    pass
            else:
                continue
main()