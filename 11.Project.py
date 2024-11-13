class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        if not self.Grades:
            return 0
        return sum(self.Grades) / len(self.Grades)

    def TotalAverage(self):
        if not self.Grades:
            return 0
        return sum(self.Grades) / len(self.Grades)

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber):
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

    def print_student_list(self):
        # Print the headers
        print(f"{'First Name':<15} {'Last Name':<15} {'ID Number':<10} {'Running Average':<15} {'Semester Average':<15} {'Letter Grade':<12}")
        print("-" * 82)
        
        # Print each student's details
        for student in self.Studentlist:
            grades_str = ', '.join(map(str, student.Grades))
            print(f"{student.FirstName:<15} {student.LastName:<15} {student.TNumber:<10} {student.RunningAverage():<15.2f} {student.TotalAverage():<15.2f} {student.LetterGrade():<12}")

    def add_student_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                firstname, lastname, tnumber = line.strip().split(',')
                self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                tnumber, *scores = line.strip().split(',')
                index = self.find_student(tnumber)
                if index != -1:
                    # Filter out empty strings and convert to integers
                    valid_scores = [int(score) for score in scores if score]
                    self.Studentlist[index].Grades.extend(valid_scores)

# Example usage:
students = StudentList()
students.add_student_from_file('11.Project Students.txt')
students.add_scores_from_file('11.Project Scores.txt')
students.print_student_list()