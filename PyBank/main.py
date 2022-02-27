

import os
import csv


months = []
profit = []
average_change = 0
total_months = 0
net_change = []


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    reader = csv.reader(csvfile)
    next(reader, None)

    for row in reader:
        month = row[0]
        months.append(month)
        values = int(row[1])
        profit.append(values)

total_months = len(months)
net_total = sum(profit)
net_total_months = len(months) - 1
difference_budget_data = []

for i in range(len(profit) - 1):
    difference_budget_data.append(float(profit[i + 1]) - float(profit[i]))
    new_net_total = sum(difference_budget_data)


average_change = new_net_total/net_total_months


min_profit = min(difference_budget_data)
max_profit = max(difference_budget_data)


print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change,2)}")
print(f'Greatest Increase in Profits: {months[profit.index(max(profit))]} (${max_profit})')
print(f"Greatest Descrease in Profits: {months[profit.index(min(profit))]} (${min_profit})")


output_file = 'Analysis/financial_analysis.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${round(average_change,2)}"])
    csvwriter.writerow([f'Greatest Increase in Profits: {months[profit.index(max(profit))]} (${max_profit})'])
    csvwriter.writerow([f"Greatest Decrease in Profits: {months[profit.index(min(profit))]} (${min_profit})"])