class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)
Employee("Rahul", "Staff").display()
print()
Trainer("Amit", "Trainer", "Weight Training").display()
print()
YogaInstructor("Neha", "Yoga Instructor", "Hatha Yoga").display()
print()
MultiTrainer("Priya", "Multi Trainer", "Cardio Training", "Vinyasa Yoga").display()