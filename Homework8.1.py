class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def info(self):
        return f"Студент: {self.first_name} {self.last_name}, Вік: {self.age}, Середній бал: {self.average_grade}"


student1 = Student("Іван", "Петренко", 20, 85)

print(student1.info())

student1.update_average_grade(92)

print(student1.info())
