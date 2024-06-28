# import library
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
total = []
changes = []
months = []

# Variables
month = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
# Read and skip the header row 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

# Function that returns the number of months
    for row in csv_reader:
        month += 1
        months.append(row[0])
# Add total to list
        total.append(int(row[1]))

# Function that returns net total
        net_total += int(row[1])

# Function to find changes
    for i in range(1, len(total)): 
        period_change = total[i] - total[i-1]
# Add changes to list
        changes.append(period_change)
# Function to find average of changes
    average_change = round(sum(changes) / len(changes),2)

# Find the greatest increase and decrease of changes list
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the month with greatest increase and decrease
increase_date = months[changes.index(greatest_increase) + 1]
decrease_date = months[changes.index(greatest_decrease) + 1]


# Print results
print('Financial Analysis')
print('----------------------------')
print('Total months: ', month)
print('Total: $', net_total)
print('Average Change: $', average_change)
print('Greatest Increase in Profits: ', increase_date, '($', greatest_increase, ')')
print('Greatest Decrease in Profits: ', decrease_date, '($', greatest_decrease, ')')

# Print to text file
with open('Financial Analysis.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write('Total months: ' + repr(month) + '\n')
    f.write('Total: $' + repr(net_total) + '\n')
    f.write('Average Change: $' + repr(average_change) + '\n')
    f.write(f"Greatest Increase in Profits: {increase_date} ($ {greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {decrease_date} ($ {greatest_decrease})") 

    