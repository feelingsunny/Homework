#Dependencies
import os
import csv

# import file
curr_path = os.path.abspath(os.path.dirname(__file__))
csvpath = os.path.join (curr_path,"election_data.csv")

Total_votes = 0
candidates = []
candidate_votes = []
percentage_votes = []

# Read File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    

    for row in csvreader:
        Total_votes = Total_votes + 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
            
    for votes in candidate_votes:        
            percentage = (votes/Total_votes) * 100
            percentage = round(percentage)
            percentage = "%.3f%%" % percentage
            percentage_votes.append(percentage)
    
    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    winning_candidate = candidates[index]


    print(f"\n\nElection Results\n")
    print(f"-------------------------\n")
    print(f"Total Votes: {str(Total_votes)}")
    print("--------------------------\n")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {str(percentage_votes[i])} ({str(candidate_votes[i])})")
    print("--------------------------\n")
    print(f"Winner: {winning_candidate}\n")
    print("--------------------------\n")

file_to_output = "/Users/liuyang/Desktop/python-challenge/PyPoll/Election_Results.txt"
with open(file_to_output, "w")as txt_file:
    election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {str(Total_votes)}\n"
    "--------------------------\n"
    )
    txt_file.write(election_results)
    
    for i in range(len(candidates)):
        candidate_votes_percent = f"{candidates[i]}: {str(percentage_votes[i])} ({str(candidate_votes[i])})\n"
        txt_file.write(candidate_votes_percent)
        
    winner_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    "--------------------------\n"
    )
    txt_file.write(winner_summary)
