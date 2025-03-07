def calculate_deductions(gross_salary):
    """Calculates and displays salary deductions and net salary."""
    
    SSS_CONTRIBUTION = 1200
    PHILHEALTH_RATE = 0.05
    PAGIBIG_CONTRIBUTION = 100
    FIXED_TAX = 1875  # Assuming a fixed tax value for simplicity

    # Compute deductions
    philhealth_contribution = (gross_salary * PHILHEALTH_RATE) / 2
    total_deductions = SSS_CONTRIBUTION + philhealth_contribution + PAGIBIG_CONTRIBUTION + FIXED_TAX
    net_salary = gross_salary - total_deductions

    # Display results
    print("\nSalary Breakdown:")
    print(f"Gross Salary: {gross_salary:.2f}")
    print(f"SSS Deduction: {SSS_CONTRIBUTION:.2f}")
    print(f"PhilHealth Deduction: {philhealth_contribution:.2f}")
    print(f"Pag-IBIG Deduction: {PAGIBIG_CONTRIBUTION:.2f}")
    print(f"Tax Deduction: {FIXED_TAX:.2f}")
    print(f"Total Deductions: {total_deductions:.2f}")
    print(f"Net Salary: {net_salary:.2f}")

# Get user input
try:
    monthly_salary = float(input("Enter your monthly salary: "))
    calculate_deductions(monthly_salary)
except ValueError:
    print("Invalid input! Please enter a valid numeric salary.")