#capturing user inputs
worker_name = input("\nPlease enter your Name: ")
task_name = input("\nPlease enter your Task Done: ")
hours_worked = int(input("\nPlease enter Hours Worked: "))
RATE = 30000

#computations
wage = hours_worked * RATE
allowance = wage * 0.05
gross_wage = allowance + wage
tax = gross_wage * 0.05
net_wage = gross_wage - tax

#output
print(f"\nName:\t\t{worker_name}\n\nTask Done:\t{task_name} \n\nTime Worked:\t{hours_worked}\n\nWage\t\t=\t{wage}\n\nAllowance\t=\t{allowance} \n\nGross Wage\t=\t{gross_wage}\n\nTax\t\t=\t{tax} \n\nNet Wage\t=\t{net_wage} \n\n")