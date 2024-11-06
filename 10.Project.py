class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [float(score) if score else 0.0 for score in scores]

    def RunningAverage(self):
        nonblankscores = [score for score in self.Grades if score != 0.0]
        if nonblankscores:
            return sum(nonblankscores) / len(nonblankscores)
        return 0.0

    def TotalAverage(self):
        return sum(self.Grades) / len(self.Grades)

    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

def readstudents(filepath):
    students = []
    with open(filepath, 'r') as file:
        for line in file:
            firstname, lastname, tnumber, *scores = line.strip().split(',')
            students.append(Student(firstname, lastname, tnumber, scores))
    return students

def printstudentreport(students):
    print(f"{'First Name':<12} {'Last Name':<12} {'ID':<12} {'Running Average':<15} {'Semester Average':<15} {'Letter Grade':<12}")
    print('-' * 72)
    for student in students:
        print(f"{student.FirstName:<12} {student.LastName:<12} {student.TNumber:<12} {student.RunningAverage():<15.2f} {student.TotalAverage():<15.2f} {student.LetterGrade():<12}")

# Example usage
students = readstudents('10.Project Student Scores.txt')
printstudentreport(students)