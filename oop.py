class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        print()


if __name__ == "__main__":
    a = Student("a", 12)
    print(a.name, a.age)

