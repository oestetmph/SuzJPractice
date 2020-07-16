def grade_average():
    """This function averages inputted grades"""
    total = 0
    grade_counter = 0
    grades = [100, 77.78, 91.67, 96.67, 85]

    for grade in grades:
        total += grade
        grade_counter += 1

    average = total / grade_counter
    print(f'The average of numbers is {average}')
