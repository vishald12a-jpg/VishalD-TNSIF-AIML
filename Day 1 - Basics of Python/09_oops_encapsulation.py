class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark  # Private attribute

    def display(self):
        print("Name:", self.name)
        print("Mark:", self.__mark)

student = Student("Arun", 85)
student.display()