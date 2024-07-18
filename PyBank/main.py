import csv

# CSV file path
file_path = "/Users/andrewsobiech/Desktop/Classwork/UNCC-VIRT-DATA-PT-06-2024-U-LOLC-main/github repositories/python-challenge/PyBank/Resources/budget_data.csv"

# Initialize variables
total_months = 0
total_profit_losses = 0
changes = []
previous_value = None
greatest_increase = ['Date', 0]
greatest_decrease = ['Date', 0]

# Read CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        total_months += 1
        current_profit_losses = int(row[1])
        total_profit_losses += current_profit_losses

        # Calculate changes in profits/losses
        if previous_value is not None:
            change = current_profit_losses - previous_value
            changes.append(change)

            # Greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            # Greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        previous_value = current_profit_losses

# Calculate average of changes, handle division by zero
if changes:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# Print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export a text file with the results
with open('financial_analysis_results.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
