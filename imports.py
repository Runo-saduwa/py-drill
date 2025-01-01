

homework_assigment_grades = {
  'homework_1': 85,
  'homework_2': 100,
  'homework_3': 81
}

def calculate_homework(arg): 
    sum_of_grades = 0
    for homework in arg.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(arg), 2)
    print(final_grade)


calculate_homework(homework_assigment_grades)