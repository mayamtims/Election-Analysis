#The data we need to retrieve:
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular votes

import csv 
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes = 0

#Candidate options
candidate_options = []
#Candidate votes
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Read and analyze data here
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #Add total vote count
         total_votes += 1
        #Print the candidate name from each row
         candidate_name = row[2]
        #If the candidate does not match any existing candidate..
         if candidate_name not in candidate_options:
             #Add it to the list of candidates
             candidate_options.append(candidate_name)
             #Begin tracking candidate vote count
             candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's name
         candidate_votes[candidate_name] += 1

#Save results to a text file
with open(file_to_save, "w") as txt_file:

#Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file 
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #Print each candidate's name, vote count and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #Save the candidate results to our text file
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage  
            winning_candidate = candidate_name 

    #Winning candidate results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save winning candidat's name to text file
    txt_file.write(winning_candidate_summary)


