class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
        
student1 = Student("John Wick", 4.0)
student2 = Student("Kamina", 2.5)
student3 = Student("Kafka", 3.3)

print(student2.get_info())
print(student1.get_info())
print(student3.get_info())

print(Student.get_count())
print(Student.get_average_gpa())