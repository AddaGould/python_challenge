import os
import csv

budget_file = r'C:\Users\Adda\OneDrive\Bootcamp\Class Folder\Module 3\3 Challenge\python-challenge-1\python_challenge\Starter_Code\PyBank\Resources\budget_data.csv'

with open(budget_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    rows = list(csvreader)

def financial_analysis(rows):
    months = len(rows)
    total = sum(int(row[1]) for row in rows)

    profit_values = []
    greatest_increase = 0
    greatest_decrease = 0

#lines 20 to 23 from learning assitant:
    for i in range(1, len(rows)):
        current_profit = int(rows[i][1])
        previous_profit = int(rows[i - 1][1])
        profit_change = current_profit - previous_profit
        profit_values.append(profit_change)
#lines 26 to 32 from ChatGPT
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_increase_month = rows[i][0]

        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_month = rows[i][0]

    average_change = sum(profit_values) / (months - 1)

    print("Financial Analysis:")
    print(f"Total Months: {str(months)}")
    print(f"Total: ${str(total)}")
    print(f"Average Change: {average_change: .2f}")
    print(f"Greatest Increase in Profits: {str(greatest_increase_month)} ${str(greatest_increase)}")
    print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} ${str(greatest_decrease)}")           
    
#instructions on how to print to .txt file from Stackoverflow:
    with open("FinancialAnalysis.txt", "w") as f:
        print("Financial Analysis:", file=f)
        print("-----------------------", file=f)
        print(f"Total Months: {str(months)}", file=f)
        print(f"Total: ${str(total)}", file=f)
        print(f"Average Change: ${average_change: .2f}", file=f)
        print(f"Greatest Increase in Profits: {str(greatest_increase_month)} ${str(greatest_increase)}", file=f)
        print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} ${str(greatest_decrease)}", file=f)

financial_analysis(rows)