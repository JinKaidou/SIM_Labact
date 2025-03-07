class SalaryCalculator:
    
    SSS_CONTRIBUTION = 1200
    PHILHEALTH_RATE = 0.05
    PAGIBIG_CONTRIBUTION = 100
    FIXED_TAX = 1875 

    def __init__(self, gross_salary):
        self.gross_salary = gross_salary

    def calculate_philhealth(self):
        """Calculates PhilHealth contribution (shared between employee and employer)."""
        return (self.gross_salary * self.PHILHEALTH_RATE) / 2

<<<<<<< HEAD
    def calculate_total_deductions(self):
        """Calculates total deductions (SSS, PhilHealth, Pag-IBIG, and Tax)."""
        philhealth = self.calculate_philhealth()
        total_deductions = (
            self.SSS_CONTRIBUTION
            + philhealth
            + self.PAGIBIG_CONTRIBUTION
            + self.FIXED_TAX
        )
        return total_deductions

    def calculate_net_salary(self):
        """Calculates net salary after deductions."""
        total_deductions = self.calculate_total_deductions()
        return self.gross_salary - total_deductions

    def display_salary_details(self):
        """Displays the salary breakdown (gross salary, deductions, and net salary)."""
        philhealth = self.calculate_philhealth()
        total_deductions = self.calculate_total_deductions()
        net_salary = self.calculate_net_salary()

        print("\nSalary Breakdown:")
        print(f"Gross Salary: {self.gross_salary:.2f}")
        print(f"SSS Deduction: {self.SSS_CONTRIBUTION:.2f}")
        print(f"PhilHealth Deduction: {philhealth:.2f}")
        print(f"Pag-IBIG Deduction: {self.PAGIBIG_CONTRIBUTION:.2f}")
        print(f"Tax Deduction: {self.FIXED_TAX:.2f}")
        print(f"Total Deductions: {total_deductions:.2f}")
        print(f"Net Salary: {net_salary:.2f}")



if __name__ == "__main__":
    try:
        monthly_salary = float(input("Enter your monthly salary: "))
        calculator = SalaryCalculator(monthly_salary)
        calculator.display_salary_details()
    except ValueError:
        print("Invalid input! Please enter a valid numeric salary.")
=======
#User input
try:
    monthly_salary = float(input("Enter your monthly salary: "))
    calculate_deductions(monthly_salary)
except ValueError:
    print("Invalid input! Please enter a valid numeric salary.")
>>>>>>> d4f78d1702b3b17376fa4183ff947ea2e7f12838
