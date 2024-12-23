class Employee:
    def __init__(self, name, id, **kwargs):
        self.name = name
        self.id = id
        super().__init__(**kwargs)

    def get_info(self):
        return "Имя: {}, ID: {}".format(self.name, self.id)


class Manager(Employee):
    def __init__(self, name, id, department, **kwargs):
        self.department = department
        super().__init__(name=name, id=id, **kwargs)

    def get_info(self):
        return "Имя: {}, ID: {}, Отдел: {}".format(self.name, self.id, self.department)

    def manage_project(self):
        return "Менеджер {} управляет проектом в отделе <<{}>>".format(self.name, self.department)


class Technician(Employee):
    def __init__(self, name, id, specialization, **kwargs):
        self.specialization = specialization
        super().__init__(name=name, id=id, **kwargs)

    def get_info(self):
        return "Имя: {}, ID: {}, Специализация: {}".format(self.name, self.id, self.specialization)

    def perform_maintenance(self):
        return "Техник {} осуществляет тех обслуживание в области <<{}>>".format(self.name, self.specialization)


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        super().__init__(name=name, id=id, department=department, specialization=specialization)
        self.team = []

    def get_info(self):
        return "Имя: {}, ID: {}, Отдел: {}, Специализация: {}".format(self.name, self.id, self.department, self.specialization)

    def add_employee(self, emp):
        self.team.append(emp)

    def get_team_info(self):
        return "Команда:\n" + "\n".join([i.get_info() for i in self.team])


ivan = Employee("Иван", "101")
anya = Manager("Анастасия", "102", "IT")
pavel = Technician("Павел", "103", "Электроника")
alex = TechManager("Алексей", "104", "Разработка", "Програмное обеспечение")

print(ivan.get_info())
print(anya.get_info())
print(pavel.get_info())
print(alex.get_info())

print(anya.manage_project())
print(pavel.perform_maintenance())
print(alex.manage_project())
print(alex.perform_maintenance())

alex.add_employee(ivan)
alex.add_employee(anya)
alex.add_employee(pavel)

print(alex.get_team_info())
