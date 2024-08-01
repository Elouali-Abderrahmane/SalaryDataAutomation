with open("employees_data.txt") as file:
    employees_data = file.readlines()

with open("updated_employee_data.txt", "w") as f:
    for employee in employees_data:
        emp = employee.strip().split(" - ")
        salary = float(employee.strip().split(" - ")[-1]) * 2
        f.write(f"{emp[0]} - {emp[1]} - {emp[2]} - {salary}\n")

