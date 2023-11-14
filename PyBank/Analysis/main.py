# Import modules
import os
import csv

# Connect csv path
budget_csv = os.path.join("Resources", "budget_data.csv")

# Define the variables 
num_months = 0
net_total = 0
amount_chng = 0
monthly_chng = []
grtincrease = 0
grtdecrease = 0 

# Open and read csv file 
with open(budget_csv) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    
    # read the header row first 
    csv_header = next(csvfile)
  
# Create lists for each of the header categories 
    months = []
    P_Ls = []
  
  # Looping through all rows and assigning variables
    for row in budget_reader:
        month = row[0]
        profit_loss = row[1]
        
        # Appending the rows to their appropriate list
        months.append(month)
        P_Ls.append(profit_loss)
    
    # Count the number of months in the months list
    num_months = len(months)
   
   # Calculate the net total amount of "Profit/Losses" over the entire period
    for element_1 in range(0, len(P_Ls)):
        net_total = net_total + int(P_Ls[element_1])
    
    # Calculate and Store changes in profits and losses in a list
    for i in range(1, num_months):
        change = int(P_Ls[i]) - int(P_Ls[i-1])
        monthly_chng.append(change)

    # Calculate average change
    average_chng = sum(monthly_chng) / len(monthly_chng)

    # Calculate the greatest increase 
    grtincrease = max(monthly_chng)

    # Calculate the greatest increase month
    grtincrease_mon = months[monthly_chng.index(grtincrease) + 1]

    # Calculate the greatest decrease 
    grtdecrease = min(monthly_chng)

    #Calculate the greatest decrease month
    grtdecrease_mon = months[monthly_chng.index(grtdecrease) + 1]

    # Print the results in a table
    with open('PyBank.txt', 'w') as output_file:
        print("Financial Analysis", file=output_file)
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _", file=output_file)
        print(f'Total Months: {num_months}', file=output_file) 
        print(f'Total: ${net_total}', file=output_file)
        print(f'Average Change: ${average_chng}', file=output_file)
        print(f'Greatest Increase in Profits: {grtincrease_mon} (${grtincrease})', file=output_file)
        print(f'Greatest Decrease in Profits: {grtdecrease_mon} (${grtdecrease})', file=output_file)