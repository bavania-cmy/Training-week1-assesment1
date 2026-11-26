import csv
from pathlib import Path


#  Bonus function with *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    """Calculates total bonus with optional extras and a maximum cap."""
    total = (salary * rate) + sum(extras)
    if "cap" in options and total > options["cap"]:
        return options["cap"]
    return total


#  Custom Exception
class InvalidSalaryError(Exception):
    """Raised when an employee is initialized with a negative salary."""
    pass


#  Employee and Manager Classes
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Employee: {self.name}, Monthly Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"Manager: {self.name}, Monthly Salary: {self.salary}, Team Size: {self.team_size}"


# Helper function to read your employees.csv
def load_employees(csv_path):
    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            row["id"] = int(row["id"])
            row["salary"] = int(float(row["salary"]))
            data.append(row)
        return data


if __name__ == "__main__":
    csv_file = Path(__file__).resolve().parent.parent / "data" / "employees.csv"
    employees = load_employees(csv_file)

    # Comprehensions, map/lambda, and filter using your CSV data
    above_50k = [emp["name"] for emp in employees if emp["salary"] > 50000]
    raised_salaries = list(map(lambda emp: round(emp["salary"] * 1.10, 2), employees))
    chennai_employees = [emp["name"] for emp in filter(lambda emp: emp["city"] == "Chennai", employees)]

    print(f"Above 50000: {above_50k}")
    print(f"Chennai: {chennai_employees}")

    # Exception Handling demonstration
    try:
        bad_emp = Employee("TestUser", -500)
    except InvalidSalaryError as e:
        print(f"Error: {e}")
    finally:
        print("Transaction finished")

    # Loop with continue (skip 0) and break (stop after first salary > 85000)
    salaries_to_check = [0] + [emp["salary"] for emp in employees]
    for sal in salaries_to_check:
        if sal == 0:
            continue
        if sal > 85000:
            break