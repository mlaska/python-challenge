import os
import csv
import operator
import collections

election_data = os.path.join('election_data.csv')

with open(election_data, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')  #this it the info to read the csv
    header = next(csvreader) #use this to skip the header row
    vote_for = []
    for row in csvreader:
        vote_for.append(row[2])
counter = len(vote_for)        
summary = collections.Counter(vote_for) 
    
print(f'Election Results')
print("--------------------------")
print(f"Total Votes: {counter}")
print("--------------------------")
for person in summary:
    print (f"{person}: {round((summary[person]/counter)*100,0)}% ({summary[person]})")
print("--------------------------")
for person, count in summary.most_common(1):
    print (f" Winner: {person}")
print("--------------------------")

with open('PyPoll_results.csv', mode='w',newline='') as mycsv:
    filewriter = csv.writer(mycsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Election Results'])
    filewriter.writerow(["--------------------------"])
    filewriter.writerow([f"Total Votes: {counter}"])
    filewriter.writerow(["--------------------------"])
    for person in summary:
        filewriter.writerow([f"{person}: {round((summary[person]/counter)*100,0)}% ({summary[person]})"])
    filewriter.writerow(["--------------------------"])
    for person, count in summary.most_common(1):
        filewriter.writerow([f" Winner: {person}"])
    filewriter.writerow(["--------------------------"])