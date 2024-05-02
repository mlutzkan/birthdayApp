import pandas as pd
import Employee

guardians_file = 'data/guardians-birthday-calendar.xlsx'


def create_employees_from_dicts(employees, team, email_ext):
    # Extracting individual dictionaries
    month_dict = employees[0]['Month']
    day_dict = employees[1]['Day']
    name_dict = employees[2]['Name']

    employees_list = []

    # Iterating over the name dictionary to create Employee instances
    for index, name in name_dict.items():
        parts = name.split()
        first_name = parts[0]
        last_name = parts[-1]
        email = f"{first_name.lower()}.{last_name.lower()}@{email_ext}"  # Change domain as needed
        birthday = f"{day_dict[index]}-{month_dict[index]}"  # Assuming day comes first in the birthday format
        employee = Employee.Employee(first_name, last_name, email, birthday, team,
                                     upcoming_birthday=False, group_created=False)
        employees_list.append(employee)

    return employees_list


def create_employees_from_xls(file, team, mail_ext):
    df = pd.read_excel(guardians_file)
    df_dict = df.to_dict()
    employees = [{key: value} for key, value in df_dict.items()]
    return create_employees_from_dicts(employees, team, mail_ext)
