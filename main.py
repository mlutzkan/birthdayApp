import Employee

Employee.add_employee("Martin", "Lutzkanov", "mlutzkan@gmail.com", "20-02-1992", "C4")
Employee.add_employee("John", "Smith", "johnsmith@gmail.com", "20-04-1996", "C4")
Employee.add_employee("Craig", "List", "craiglist@gmail.com", "18-02-1981", "C4")
Employee.add_employee("John", "Cena", "ucantcme@wwe.com", "11-01-1992", "C4")
Employee.add_employee("Birthday", "Boy 1", "happy@gmail.com", "22-04-1992", "C4")
Employee.add_employee("Birthday", "Boy 2", "birthday@gmail.com", "10-05-1986", "C4")

# Update the responsible persons pool
Employee.get_upcoming_birthdays()
Employee.update_responsible_persons_pool()

# Print responsible persons pool
print("Responsible Persons Pool:")
for employee in Employee.responsible_persons_pool:
    print(employee)

# Print upcoming birthdays
print("\nUpcoming Birthdays:")
for employee in Employee.upcoming_birthday_employees_list:
    employee.display_info()