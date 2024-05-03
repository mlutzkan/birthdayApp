import Employee
import getData


guardians_list = getData.create_employees_from_xls(getData.guardians_file, 'Guardians', 'strypes.eu')

guardians_upcoming_birthdays = Employee.get_upcoming_birthdays(guardians_list)
Employee.choose_money_collector(guardians_list)

# Print upcoming birthdays
print("Upcoming Birthdays:\n")
for employee in guardians_upcoming_birthdays:
    employee.display_info()
    print(f"Upcoming birthday: {employee.upcoming_birthday}")
    print(f"Group created: {employee.group_created}")
    print(f"Collector: {employee.collector}")
    print(f"Backup collector: {employee.backup_collector}\n\n")


