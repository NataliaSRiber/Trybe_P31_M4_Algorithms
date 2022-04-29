def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    students_counter = 0
    try:
        for student_period in permanence_period:
            if type(target_time) != int or type(student_period[0]) != int or type(student_period[1]) != int:
                raise ValueError
            if student_period[0] <= target_time <= student_period[1]:
                students_counter += 1
        return students_counter
    except ValueError:
        return None
