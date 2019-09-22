import os
import csv
import operator
#import locale

#locale.setlocale( locale=LC_ALL, '')
#'English_United States.1252'

# Path to collect data from the Resources folder
budget_data = os.path.join('budget_data.csv')

# Read in the CSV file
with open(budget_data, newline="") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')  #this it the info to read the csv
    header = next(csvreader) #use this to skip the header row
    counter = 0 #defining and setting the counter variable for the number of months
    Total = 0 #defining and setting the total gains/losses counter
    change = 0
    min_ctr = 0 
    max_ctr = 0
    Date_list = {}
    Change_list = []
    min_item = []
    max_item = []
    current_profit = 0
    last_profit = 0
    Max = 0
    #For every row in the file, I want to add to my counter to identify that I have ticked to the next row
    #For every row in the file, I want to add the current
    for row in csvreader:
        counter = 1 + counter
        current_profit = int(row[1])
        Total = Total + current_profit
        if counter > 1:
            change = current_profit - last_profit 
            Change_list.append(change)
            Date_list.update({row[0]:change})
        last_profit = int(row[1])
    Avg = sum(Change_list)/len(Change_list)
    max_item.append(max(Date_list.items(), key=operator.itemgetter(1))[0])
    max_item.append(max(Change_list))
    min_item.append(min(Date_list.items(), key=operator.itemgetter(1))[0])
    min_item.append(min(Change_list))
print(f'Financial Analysis')
print("-----------------------------------------")
print(f"Total Months: {counter}")
print(f"Total: ${Total}")
print(f"Average Change: $ {round(Avg,2)}")
print(f"Greatest Increase in Profits: {max_item[0]} (${max_item[1]})")
print(f"Greatest Decrease in Profits: {min_item[0]} (${min_item[1]})")


with open('PyBank_Analysis.csv', mode='w',newline='') as mycsv:
    filewriter = csv.writer(mycsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Financial Analysis'])
    filewriter.writerow([f"Total Months: {counter}"])
    filewriter.writerow([f"Total: ${Total}"])
    filewriter.writerow([f"Average Change: $ {Avg}"])
    filewriter.writerow([f"Greatest Increase in Profits: {max_item[0]} (${max_item[1]})"])
    filewriter.writerow([f"Greatest Decrease in Profits: {min_item[0]} (${min_item[1]})"])