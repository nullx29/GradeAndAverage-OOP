class GradeAndAverage:
    def __init__(self, grades):
        self.grade = grades

    def display_grades(self):
        for key, value in self.grade.items():
            print(f"{key:<10}   :   {value}/100")

    def calculate_avergae(self):
        total = sum(self.grade.values())
        no = len(self.grade.keys())
        average = total / no
        print(f"average: {average:.2f}")
        if average >= 50:
            print(f"You passed!")
        else:
            print(f"You failed!")
Ahmed_grades = {
    "Maths": 2,
    "Science": 0,
    "Sports": 100,
    "English": 80
}
Sara_grades = {
    "Maths": 99,
    "Science": 60,
    "Sports": 100,
    "English": 99
}
def startgradesclass(grades, name):
    print(f"{name}'s grades: ")
    x = GradeAndAverage(grades)
    x.display_grades()
    x.calculate_avergae()
startgradesclass(Ahmed_grades, "Ahmed")
startgradesclass(Sara_grades, "Sara")


