def grade_average():
    """This function averages inputted grades"""

    number_of_grades = int(input('Please input the number of grades: '))
    grade_total = 0
    grade_avg = 0

    for x in range(number_of_grades):
        input_grade = float(input('Grade ' + str(x + 1) + ': '))
        grade_total = grade_total + input_grade

    print('\n==================')
    print('Your Average: ' + str(round(grade_total / number_of_grades, 2)))
