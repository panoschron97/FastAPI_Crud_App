import datetime

from fastapi import FastAPI

from models import information

app = FastAPI()

employees = []

p1 = information(id = 1, firstname = "Panagiotis", lastname = "Chronopoulos", age = 28, sex = "M", datebirth = datetime.datetime.strptime("1997-03-27", "%Y-%m-%d"), jobstatus = False, levelofeducation = "6", salary = 0.0)
p1.set_salary(p1.get_net_salary())
p2 = information(id = 2, firstname = "Nikos", lastname = "Stergiou", age = 30, sex = "M", datebirth = datetime.datetime.strptime("1995-03-27", "%Y-%m-%d"), jobstatus = True, levelofeducation = "8", salary = 2500.0)
p2.set_salary(p2.get_net_salary())
p3 = information(id = 3, firstname = "Giwrgos", lastname = "Gewrgiou", age = 50, sex = "M", datebirth = datetime.datetime.strptime("1975-02-20", "%Y-%m-%d"), jobstatus = True, levelofeducation = "8", salary = 6500.0)
p3.set_salary(p3.get_net_salary())
p4 = information(id = 4, firstname = "UnKnownFirstName", lastname = "UnKnownLastName", age = 80, sex = "M", datebirth = datetime.datetime.strptime("1940-01-01", "%Y-%m-%d"), jobstatus = False, levelofeducation = "N/A", salary = 0.0)
p4.set_salary(p4.get_net_salary())

employees.append(p1)
employees.append(p2)
employees.append(p3)
employees.append(p4)

@app.get("/")
async def panos_api():
    return "Welcome to PanosAPI!"

@app.get("/api/employees")
async def get_all_employees():
    print("\n" + str(employees) + "\n")
    return employees

@app.get("/api/employees/{id}")
async def get_employee_by_id(employeeid : str):
    if not employeeid.isdigit() or (employeeid.isdigit() and int(employeeid) <= 0):
        return "You need to enter a valid and positive number!"
    else:
        for employee in employees:
            if(int(employeeid) == employee.get_id()):
                print("\n" + str(employee) + "\n")
                return employee
        else:
            return "Employee not found with id : " + employeeid

@app.post("/api/employees")
async def add_employee(employee: information):
    employee.set_salary(employee.get_net_salary())
    employees.append(employee)
    print("\n" + str(employee) + "\n")
    return employee

@app.put("/api/employees")
async def update_employee(employeeid: str, employee: information):
    if not employeeid.isdigit() or (employeeid.isdigit() and int(employeeid) <= 0):
        return "You need to enter a valid and positive number!"
    else:
        for i in range(len(employees)):
            if(employees[i].get_id() == int(employeeid)):
                employees[i] = employee
                print("\n" + str(employees[i]) + "\n")
                return "Employee updated successfully!"
        else:
            return "No employee found with id : " + employeeid

@app.delete("/api/employees/{employeeid}")
async def delete_employee(employeeid : str):
    if not employeeid.isdigit() or (employeeid.isdigit() and int(employeeid) <= 0):
        return "You need to enter a valid and positive number!"
    else:
        for employee in employees:
            if(int(employeeid) == employee.get_id()):
                employees.remove(employee)
                print("\nDeleted row - > " + str(employee) + "\n")
                return "Employee deleted successfully!"
        else:
            return "Employee not found with id : " + employeeid
