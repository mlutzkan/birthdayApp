import Employee
import getData


guardians_list = getData.create_employees_from_xls(getData.guardians_file, 'Guardians', 'strypes.eu')

guardians_upcoming_birthdays = Employee.get_upcoming_birthdays(guardians_list)
guardians_pool = Employee.update_responsible_persons_pool(guardians_list)

# Print upcoming birthdays
print("Upcoming Birthdays:\n")
for employee in guardians_upcoming_birthdays:
    employee.display_info()
    print(f"Upcoming birthday: {employee.upcoming_birthday}")
    print(f"Group created {employee.group_created}")


# Print responsible persons pool
print("\n\nResponsible Persons Pool:\n")
for employee in guardians_pool:
    print(employee)