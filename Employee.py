import datetime


class Employee:
    def __init__(self, first_name, last_name, email, birthday, team):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = datetime.datetime.strptime(birthday, "%d-%m-%Y").date()
        self.team = team

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def display_info(self):
        print("\nEmployee Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Birthday: {self.birthday.strftime('%d-%m-%Y')}")
        print(f"Team: {self.team}")


employee_list = []
responsible_persons_pool = []
upcoming_birthday_employees_list = []


# Function to add a new employee to the list.
def add_employee(first_name, last_name, email, birthday, team):
    employee = Employee(first_name, last_name, email, birthday, team)
    employee_list.append(employee)


# Function to store employees with upcoming birthdays
def get_upcoming_birthdays():
    today = datetime.date.today()
    upcoming_birthday_employees_list.clear()

    for employee in employee_list:
        # Calculate employee's birthday for this year
        birthday_this_year = datetime.date(today.year, employee.birthday.month, employee.birthday.day)

        # Calculate difference in days between today and employee's birthday
        days_until_birthday = (birthday_this_year - today).days

        # If the difference is less than or equal to 20 days, add the employee to the list
        if 0 < days_until_birthday <= 20:
            upcoming_birthday_employees_list.append(employee)

    return upcoming_birthday_employees_list


def update_responsible_persons_pool():
    responsible_persons_pool.clear()
    upcoming_birthdays = get_upcoming_birthdays()
    for employee in employee_list:
        if employee not in upcoming_birthdays:
            responsible_persons_pool.append(employee)
    return responsible_persons_pool
