import os
import csv

PyBankcsv = os.path.join('..', 'Resources', 'budget_data.csv')

profits = []
monthly_change = []
dates = []

total_profit = 0
total_change_profits = 0
count = 0
initial_profit = 0

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1 
        dates.append(row[0])
        profits.append(row[1])
        total_profit = total_profit + int(row[1])
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        monthly_change.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        average_change_profits = (total_change_profits/count)

        greatest_increase_profits = max(monthly_change)
        greatest_decrease_profits = min(monthly_change)
        increase_date = dates[monthly_change.index(greatest_increase_profits)]
        decrease_date = dates[monthly_change.index(greatest_decrease_profits)]

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------") 

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------")
    text.write("  Financial Analysis")
    text.write("----------------------------------------------------------")
    text.write("    Total Months: " + str(count) )
    text.write("    Total Profits: " + "$" + str(total_profit) )
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) )
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) )
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) )
    text.write("----------------------------------------------------------")       