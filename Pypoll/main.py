import csv

# CSV file path
file_path = "/Users/andrewsobiech/Desktop/Classwork/UNCC-VIRT-DATA-PT-06-2024-U-LOLC-main/github repositories/python-challenge/PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate results
results = []
winner = None
max_votes = 0

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file
with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for result in results:
        output_file.write(result + "\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")