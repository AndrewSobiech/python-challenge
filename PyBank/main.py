import csv

# CSV file path
file_path = 'budget_data.csv'

# initialize var
total_months = 0
total_profit_losses = 0
changes = []
previous_value = None
greatest_increase = ['Data', 0]
greatest_decrease = ['Date', 0]

# Read CSV file
with open(file_path, mode='r') as file:
  csv_reader = csv.reader(file)
  header = next(csv_reader)

  for row in csv_reader:
    total_months +=1
    current_profit_losses = int(row[1])
    total_profit_losses += current_profit_loses

# calc changes in profits/losses
if previous_valie is not None:
  change = current_proffit_losses - previous_value
  changes.append(change)

  # greatest increase in profits
  if change > greatest_increase[1]:
    greatest_increase = [row[0], change]

  #  greatest decrease in profits
  if change < greatest_decrease[1]:
    greatest_decrease = [row[0], change]

previous_value = current_profit_losses
