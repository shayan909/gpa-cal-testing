import numpy as np


def courses():
    n = int(input("enter No. of Courses:"))
    if n <= 0:
        raise ValueError("Zero Courses?")

    credits = []
    gradePoints = []

    for i in range(n):
        cred = input(f"Course {i + 1} Credits")
        grade = input(f"Course {i + 1} Grade Points")
        credits.append(cred)
        gradePoints.append(grade)

    return gradePoints, credits


def gpa_cal(grade, cred):
    weight = np.multiply(grade, cred)
    total = 0
    for i in range(0, len(cred)):
        total = total + cred[i]
    Gpa = sum(weight) / total
    return round(Gpa, 2)

