"""Exercise 1: Manage employee information using list and dictionary."""

SALARY_THRESHOLD = 10_000


def input_int(prompt):
    """Read a positive integer from the keyboard."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid number, please try again.")


def input_salary(prompt):
    """Read a non-negative salary."""
    while True:
        try:
            salary = float(input(prompt))
            if salary >= 0:
                return salary
            print("Salary cannot be negative.")
        except ValueError:
            print("Invalid salary, please try again.")


def input_employees():
    """Input employee information and store them in a list of dictionaries."""
    employees = []
    count = input_int("Enter the number of employees: ")

    for i in range(count):
        print(f"\n--- Employee {i + 1} ---")
        while True:
            employee_id = input("Employee ID: ").strip()
            if not employee_id:
                print("Employee ID cannot be empty.")
            elif any(e["id"] == employee_id for e in employees):
                print("Employee ID already exists.")
            else:
                break
        full_name = input("Full name: ").strip()
        salary = input_salary("Salary: ")

        employees.append({
            "id": employee_id,
            "name": full_name,
            "salary": salary,
        })
    return employees


def display_employees(employees, title):
    """Display a list of employees as a table."""
    print(f"\n===== {title} =====")
    if not employees:
        print("No employees found.")
        return
    print(f"{'ID':<10}{'Full name':<25}{'Salary':>12}")
    print("-" * 47)
    for e in employees:
        print(f"{e['id']:<10}{e['name']:<25}{e['salary']:>12,.2f}")


def find_highest_salary(employees):
    """Return all employees with the highest salary."""
    highest = max(e["salary"] for e in employees)
    return [e for e in employees if e["salary"] == highest]


def calculate_average_salary(employees):
    """Return the average salary of all employees."""
    return sum(e["salary"] for e in employees) / len(employees)


def find_high_salary(employees):
    """Return employees whose salary > SALARY_THRESHOLD."""
    return [e for e in employees if e["salary"] > SALARY_THRESHOLD]


def main():
    employees = input_employees()

    display_employees(employees, "ALL EMPLOYEES")
    display_employees(find_highest_salary(employees), "HIGHEST SALARY")
    print(f"\n===== AVERAGE SALARY =====\n{calculate_average_salary(employees):,.2f}")
    display_employees(find_high_salary(employees),
                      f"EMPLOYEES WITH SALARY > {SALARY_THRESHOLD:,}")


if __name__ == "__main__":
    main()
