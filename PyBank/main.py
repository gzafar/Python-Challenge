# Mpdule to create file paths across all operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Read with CSV module
with open(csvpath) as csvfile:

    # Specify the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read each row after header
    for row in csvreader:
        print(row)
