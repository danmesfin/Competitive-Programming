
def gradingStudents(grades):
    # Write your code here
    
    for i in range(len(grades)):
        if grades[i] >= 38:
            x = (grades[i]//5) + 1
            if (x*5 - grades[i]) < 3:
                grades[i] = x*5
           
    return grades
