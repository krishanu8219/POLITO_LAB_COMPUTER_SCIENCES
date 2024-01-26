#Function to compute avg and store in list for each student
def compute_avg(name_list, marks_list):
    avg_marks_list = []
    for i in range(len(name_list)):
        sum_of_marks = 0
        count = 0
        for marks in marks_list[i]:
            if marks == "N/A":
                sum_of_marks = "N/A"
                break
            else:
                sum_of_marks += float(marks)
                count += 1
        if sum_of_marks != "N/A":
            avg_marks = sum_of_marks / count
            avg_marks_list.append(avg_marks)
        else:
            avg_marks_list.append("N/A")    
    return avg_marks_list

#function to print the output
def marks_printer(name_list, avg_marks_list):
    for i in range(len(name_list)):
        print(f"Name: {name_list[i]} - Average Mark: {avg_marks_list[i]}")                

#Main Function
def main():
    student_name_list = []
    all_students_mark_list = []  

    #getting student names in a list
    while True:
        student_name = input("Enter the name of student (or press enter to continue:)")
        if student_name == "":
            break
        else:
            student_name_list.append(student_name)
        #Getting marks for every student in a list
            student_mark_list = []#sublist for student marks 
            while True:
                student_marks = input("Insert Mark (or press Enter to continue)")
                if student_marks == "":
                    if len(student_mark_list) == 0:
                        student_mark_list.append("N/A")
                        break
                    else:
                        break
                else:
                    student_mark_list.append(student_marks)
            all_students_mark_list.append(student_mark_list)        

    avg_marks_list = compute_avg(student_name_list, all_students_mark_list)
    marks_printer(student_name_list, avg_marks_list)


if __name__ == "__main__":
    main()    