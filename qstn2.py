def gradeStudent(grades):
    """
    """
    def roundingAlgo(grade):
        if grade < 38:
            return grade
        roundedGrade = 5 * round(grade/5)
        if roundedGrade < grade:
            return grade
        return roundedGrade
    return [roundingAlgo(grade) for grade in grades]


print(gradeStudent([84, 38, 57]))
