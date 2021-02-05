# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes the candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
import os
import csv

file_path = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

county_list = []
county_votes = {}

county_with_greatest_turnout = ""
county_vote_count = 0
county_vote_percentage = 0

with open(file_path) as election_data:
	file_reader = csv.reader(election_data)

	headers = next(file_reader)
	for row in file_reader:
		total_votes += 1
		county_name = row[1]
		candidate_name = row[2]

		if county_name not in county_list:
			county_list.append(county_name)
			county_votes[county_name] = 0

		if candidate_name not in candidate_options:
			candidate_options.append(candidate_name)
			candidate_votes[candidate_name] = 0

		county_votes[county_name] += 1
		candidate_votes[candidate_name] += 1



with open("election_results.txt", "w") as txt_file:
	election_results = (
		f"\nElection Results\n"
		f"-------------------------\n"
		f"Total Votes: {total_votes:,}\n"
		f"-------------------------\n")
	print(election_results)
	txt_file.write(election_results)
	print("County Votes:")
	txt_file.write("County Votes:\n")

	for county in county_list:

		votes_per_county = county_votes[county]
		vote_percentage_by_county = float(votes_per_county) / float(total_votes) * 100

		if (votes_per_county > county_vote_count) and (vote_percentage_by_county > county_vote_percentage):
			county_vote_count = votes_per_county
			county_vote_percentage = vote_percentage_by_county
			county_with_greatest_turnout = county

		county_results = f"{county}: {vote_percentage_by_county:.1f}% ({votes_per_county:,})\n"
		print(county_results)
		txt_file.write(county_results)

	county_summary = (
		f"\n-------------------------\n"
		f"Largest County Turnout: {county_with_greatest_turnout}\n"
		f"-------------------------\n")

	print(county_summary)
	txt_file.write(county_summary)

	for candidate in candidate_options:

		votes = candidate_votes[candidate]
		vote_percentage = float(votes) / float(total_votes) * 100

		if (votes > winning_count) and (vote_percentage > winning_percentage):
			winning_count = votes
			winning_percentage = vote_percentage
			winning_candidate = candidate

		candidate_results = f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
		print(candidate_results)
		txt_file.write(candidate_results)

	winning_candidate_summary = (
	f"-------------------------\n"
	f"Winner: {winning_candidate}\n"
	f"Winning Vote Count: {winning_count:,}\n"
	f"Winning Percentage: {winning_percentage:.1f}%\n"
	f"-------------------------\n")

	print(winning_candidate_summary)
	txt_file.write(winning_candidate_summary)