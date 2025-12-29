import random


class Student:
    def __init__(self, name, subjects_pool):
        self.name = name
        self.subjects_pool = subjects_pool  
        self.schedule = {}                  # расписание: день - список предметов
        self.grades = {}                    # оценки: предмет 

    def generate_week_schedule(self):
        
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

        self.schedule.clear()

        for day in days:
            count = random.randint(2, 3)  # 2 или 3 предмета в день

            self.schedule[day] = random.choices(self.subjects_pool, k=count)

    def generate_grades(self):

        self.grades.clear()

        # соберём все предметы, которые встретились в расписании
        all_subjects = set()
        for subjects_in_day in self.schedule.values():
            all_subjects.update(subjects_in_day)

        # генерируем оценки
        for subject in all_subjects:
            marks_count = random.randint(1, 3)  # сколько оценок по предмету
            self.grades[subject] = [random.randint(1, 12) for _ in range(marks_count)]
    def show_schedule(self):

        
        print(f"\nРасписание студента: {self.name}")
        for day, subjects in self.schedule.items():
            print(f"\n{day}: " + ", ".join(subjects))

    def show_grades(self):
        
        print(f"\nОценки студента: {self.name}")
        for subject, marks in self.grades.items():
            marks_str = ", ".join(map(str, marks))
            print(f"{subject}: {marks_str}")

    def average_grade(self):
        
        all_marks = []
        for marks in self.grades.values():
            all_marks.extend(marks)

        if len(all_marks) == 0:
            return 0.0

        return sum(all_marks) / len(all_marks)


class Stipendiya:
    def calculate(self, student: Student):
        #Рассчитываем стипендию по средней оценке
        avg = student.average_grade()


        if avg >= 10:
            return 2000
        elif avg >= 8:
            return 1500
        elif avg >= 6:
            return 1000
        else:
            return 0



def start():
    subjects = [
        "Математика", "Физика", "Информатика", "История",
        "Украинский язык", "Английский язык", "Химия", "Биология"
    ]

    student = Student(input("Введите имя студента:"), subjects)

    # генерируем расписание и оценки
    student.generate_week_schedule()
    student.generate_grades()

    # выводим
    student.show_schedule()
    student.show_grades()

    avg = student.average_grade()
    print(f"\nСредний балл: {avg:.2f}")

    stipend = Stipendiya()
    money = stipend.calculate(student)
    print(f"Стипендия: {money} грн")

start()