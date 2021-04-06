import os
import csv

PyBankcsv = os.path.join('..', 'Resources', 'election_data.csv')

count = 0

vote_count = []
unique_candidate = []
vote_percent = []
candidatelist = []

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election Results")
    text.write("---------------------------------------")
    text.write("Total Vote: " + str(count) + "")
    text.write("---------------------------------------")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")")
    text.write("---------------------------------------")
    text.write("The winner is: " + winner )
    text.write("---------------------------------------")