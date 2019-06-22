#Dependencies
import os
import csv

# import file
curr_path = os.path.abspath(os.path.dirname(__file__))
csvpath = os.path.join (curr_path,"budget_data.csv")

# Begin variables
Total_Months = 0
Total_pl= 0 
prev_change = 0

dates = []
change_list = []

# Read File
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    

    for row in csvreader:
        
        Total_Months = Total_Months + 1
        Total_pl = Total_pl + int(row[1])
        dates.append(row[0])

        change = int(row[1]) - prev_change
        prev_change = int(row[1])
        change_list.append(change)

change_list.pop(0)
avg_change = sum(change_list)/len(change_list)
     
greatest_increase = max(change_list)
greatest_index = change_list.index(greatest_increase)
greatest_date = dates[greatest_index+1]

greatest_decrease = min(change_list)
worst_index = change_list.index(greatest_decrease)
worst_date = dates[worst_index+1]

#Generate output analysis

output = (
    f"\nFinancial Analysis\n"
    f"---------------------\n"
    f"Total Months: {str(Total_Months)}\n"
    f"Total: ${str(Total_pl)}\n"
    f"Average Change: ${str(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})\n"
)

print(output)

#Export the results to text file
file_to_output = "/Users/liuyang/source/DataViz/Homework/03-Python/PyBank/PyBank_analysis.txt"
with open(file_to_output, "w")as txt_file:
    txt_file.write(output)
