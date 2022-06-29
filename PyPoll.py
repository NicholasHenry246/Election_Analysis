# Find:
# The total number of votes case
# The complete list of candidates who received votes
# The percentage votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on the popular vote
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file to the path 
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open ELection results and read file
#Initialize total vote counter

total_votes = 0

#Open Election results and read file
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
# Read the headers

    Headers = next(file_reader)

#Print each row in the csv file

    for row in file_reader:
    
    # Add the total vote count
        total_votes += 1

        candidate_name = row[2]

        #Add the candidate name to the candidate list using append and if statement

        if candidate_name not in candidate_options:
# Adding candidates to the list if not already in the list
            candidate_options.append(candidate_name)
# Tracking the candidates vote count
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes)/float(total_votes)*100

        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # print(winning_candidate_summary)






    




