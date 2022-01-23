# The Data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Assign a variable for the file to load and the path.

from calendar import calendar
import os
import csv
dir (os)

# Assign a variable for the file to load the path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter 
total_votes = 0

#Candidate options & Candidate votes
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#Open the election results and read the file
with open(file_to_load) as election_data:
    
    #To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    #Print each row in the csv file:
    for row in file_reader:
    
        #Increment total votes by 1
        total_votes += 1
        
        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
                #Add it to the list of candidates
                candidate_options.append(candidate_name)

                #2 Begin tracking that candidate's vote count
                candidate_votes[candidate_name] = 0

        #3 Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2 Retreive vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = (float(votes)) / float(total_votes)*100
    

    #To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2 If true then set winning_count = votes and winning_percent = 
            #vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

#To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
    
winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------------\n")
print(winning_candidate_summary)


