# import library
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")
 
# Lists to store data
candidate_names = []
found_candidates = []
count_per = []
candidate_votes = []
candidate_list = []

# Set variables
net_votes = 0
vote_for_candidate = 0
last_count = 0


# Set path for election_data csvfile
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
# Read and skip the header row 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        candidate_names.append(row[2])
# Tally all votes
        net_votes += 1

# Print this here to print in the correct order
print('Election Results')
print('-------------------------')
print('Total Votes:', net_votes)
print('-------------------------')

# Find each unique name and put it in the list
for name in candidate_names:
    if name not in found_candidates:
        found_candidates.append(name)


# Loop to find the votes for all candidates and then the percentage of their total vote
for individual_candidate in found_candidates:
    for vote in candidate_names:
        if individual_candidate == vote:
            vote_for_candidate += 1
    percent = vote_for_candidate/len(candidate_names)

    
    

    if last_count < vote_for_candidate:
        Winner = individual_candidate
    print(f"{individual_candidate}: {percent:.3%} ({vote_for_candidate})")
    
# Create lists to print to text
    count_per.append(percent)
    candidate_votes.append(vote_for_candidate)
    candidate_list.append(individual_candidate)
    
# Resets at zero for each candidate as they loop
    last_count = vote_for_candidate
    vote_for_candidate = 0


# Print the rest of the results
print("---------------------")
print(f"Winner: {Winner}")
print("---------------------")



# Print to text file
with open('election_analysis', "w") as f:
    f.write('Election Results\n')
    f.write('-------------------------\n')
    f.write(f'Total Votes: {net_votes}\n')
    f.write('-------------------------\n')
    for i in range(len(found_candidates)):
        f.write(f'{candidate_list[i]}: {count_per[i]:.3%} ({candidate_votes[i]})\n')
    f.write('------------------------\n')
    f.write(f'Winner: {Winner}')
























