import datetime
import random
import secrets


class Employee:
    def __init__(self, first_name, last_name, email, birthday, team, upcoming_birthday, group_created, collector,
                 backup_collector):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = datetime.datetime.strptime(birthday, "%d-%m").date()
        self.team = team
        self.upcoming_birthday = upcoming_birthday
        self.group_created = group_created
        self.collector = collector
        self.backup_collector = backup_collector

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Birthday: {self.birthday.strftime('%d-%m')}")
        print(f"Team: {self.team}")


# employee_list = []
# responsible_persons_pool = []
# upcoming_birthday_employees_list = []


# Function to add a new employee to the list.
def add_employee(employee_list, first_name, last_name, email, birthday, team, collector):
    employee = Employee(first_name, last_name, email, birthday, team, upcoming_birthday=False,
                        group_created=False, collector=None, backup_collector=None)
    employee_list.append(employee)


# Function to store employees with upcoming birthdays
def get_upcoming_birthdays(employee_list):
    today = datetime.date.today()
    upcoming_birthday_employees_list = []

    for employee in employee_list:
        # Calculate employee's birthday for this year
        birthday_this_year = datetime.date(today.year, employee.birthday.month, employee.birthday.day)

        # Calculate difference in days between today and employee's birthday
        days_until_birthday = (birthday_this_year - today).days

        # If the difference is less than or equal to 20 days, add the employee to the list
        if 0 < days_until_birthday <= 20:
            employee.upcoming_birthday = True
            upcoming_birthday_employees_list.append(employee)

    return upcoming_birthday_employees_list


def update_responsible_persons_pool(employee_list):
    responsible_persons_pool = []
    upcoming_birthdays = get_upcoming_birthdays(employee_list)
    for employee in employee_list:
        if employee not in upcoming_birthdays:
            responsible_persons_pool.append(employee)
    return responsible_persons_pool


def choose_money_collector(employee_list):
    pool = update_responsible_persons_pool(employee_list)
    for employee in employee_list:
        first_choice = random.choice(pool)
        employee.collector = first_choice
        second_choice = random.choice(pool)
        while second_choice == first_choice:
            second_choice = random.choice(pool)
        employee.backup_collector = second_choice



