# Module to create file paths across all operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists of all the months & profits
months = []
net_total = []
changes = []

# Set variables
i = 0

# Read with CSV module
with open(csvpath) as csvfile:

    # Specify the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read header row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row after header
    for row in csvreader:
        
        # Add totals to list
        months.append(row[0])
        net_total.append(int(row[1]))
        changes.append(int(row[1])-i)

        i = int(row[1])

    # Remove first (header) row when calculating monthly changes        
    changes.pop(0)

    print(len(changes))

    # Count all the months in data set
    total_months = len(months)

    # Calculate sum (net total)
    total_profit = sum(net_total)

    # Calculate sum of all changes
    total_changes = sum(changes)

    # Calculate average change
    average_change = round(total_changes/len(changes), 2)

    # Greatest increase & decrease in profits
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    # Find the months for greatest increase & decrease in profits
    increase_month = months[(changes.index(greatest_increase))]
    decrease_month = months[(changes.index(greatest_decrease))]

# Print final answers
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profit}")   
print(f"Average Change: ${average_change}") 
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Export text file
Financial_Analysis = open("Financial_Analysis.txt","w")
Financial_Analysis.write("Financial Analysis\n")
Financial_Analysis.write("----------------------------\n")
Financial_Analysis.write(f"Total Months: {total_months}\n")
Financial_Analysis.write(f"Average Change: ${average_change}\n")
Financial_Analysis.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
Financial_Analysis.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")
Financial_Analysis.close() 