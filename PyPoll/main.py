# Mpdule to create file paths across all operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Read with CSV module
with open(csvpath) as csvfile:

    # Specify the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Total vote counter & list
    total_votes = 0
    votes = []
    
    # Create a list & dictionary to hold candidates' names
    candidates = []
    dict_of_candidates = {}
    candidate_votes = {}

    # Set variables 
    i = 0

    #  header row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Loop through each row after header
    for row in csvreader:
        
        # Add totals to a list
        votes.append(row[0])

        i = int(row[0])

        # Count all votes in data set
        total_votes = len(votes)

        # Check if candidate is in dictionary of candidates
        if row[2] not in dict_of_candidates.keys():
            dict_of_candidates[row[2]] = 1

        # Add to list if candidate comes up
        else:
            dict_of_candidates[row[2]] += 1

winner = max(dict_of_candidates, key=dict_of_candidates.get) 

for candidates in dict_of_candidates.keys():
    candidate_name = ""
    votes.append(candidate_name)
    candidate_name = '\n'.join([candidate_name + "{:.2%}".format(dict_of_candidates[candidates] / total_votes) + "(" + str(dict_of_candidates[candidates]) + ")" ])

# Print final answers
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(candidates, "{:.2%}".format(dict_of_candidates[candidates] / total_votes) + " (" + str(dict_of_candidates[candidates]) + ")")
print("----------------------------")
print(f"Winner: {(winner)}")

# Export text file
Election_Results = open("Election_Results.txt","w")
Election_Results.write("Election Results\n")
Election_Results.write("----------------------------\n")
Election_Results.write(f"Total Votes: {total_votes}\n")
Election_Results.write("----------------------------\n")
Election_Results.write("{candidate_name}\n")
Election_Results.write("----------------------------\n") 
Election_Results.write(f"Winner: {(winner)}\n")
Election_Results.close() 