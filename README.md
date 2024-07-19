# python-challenge
Homework Module 3 working in python

# PyPoll - Election Results Analysis

# Overview

The script analyzes election data from a CSV file and provides the following results:

- The total number of votes cast.
- A complete list of candidates who received votes.
- The percentage of votes each candidate won.
- The total number of votes each candidate won.
- The winner of the election based on popular vote.

The results are printed to the terminal and exported to a text file named `election_results.txt`.

# Data

The data is provided in a CSV file located at:
/Users/andrewsobiech/Desktop/Classwork/UNCC-VIRT-DATA-PT-06-2024-U-LOLC-main/github repositories/python-challenge/PyPoll/Resources/election_data.csv

# Script 

The script performs the following steps:

1. **Read the CSV file**:
   - Opens the CSV file in read mode.
   - Skips the header row.

2. **Initialize Variables**:
   - `total_votes`: To count the total number of votes cast.
   - `candidate_votes`: A dictionary to store the votes received by each candidate.

3. **Process Each Row**:
   - Iterates through each row in the CSV file.
   - Increments the total vote count.
   - Updates the vote count for each candidate.

4. **Calculate Results**:
   - Calculates the percentage of votes each candidate received.
   - Identifies the candidate with the maximum votes as the winner.

5. **Print Results**:
   - Prints the election results to the terminal.

6. **Export Results**:
   - Exports the results to a text file named `election_results.txt`.
  


**PyBank - Financial Analysis**

# Overview

The script analyzes financial data from a CSV file and provides the following results:

- The total number of months included in the dataset.
- The net total amount of "Profit/Losses" over the entire period.
- The average of the changes in "Profit/Losses" over the entire period.
- The greatest increase in profits (date and amount) over the entire period.
- The greatest decrease in profits (date and amount) over the entire period.
  
The results are printed to the terminal and exported to text file named `financial_analysis_results.txt`.

# Data

The data is provided in a CSV file located at:
/Users/andrewsobiech/Desktop/Classwork/UNCC-VIRT-DATA-PT-06-2024-U-LOLC-main/github repositories/python-challenge/PyBank/Resources/budget_data.csv

# Script Details

The script performs the following steps:

1. **Read the CSV file**
   - Opens the CSV file in read mode.
   - Skips the header row.

2. **Initialize Variables**
   - `total_months`: To count the total number of months included in the dataset.
   - `total_profit_losses`: To sum the net total amount of "Profit/Losses".
   - `changes`: To store the monthly changes in "Profit/Losses".
   - `previous_value`: To keep track of the previous month's "Profit/Losses".
   - `greatest_increase`: To store the greatest increase in profits (date and amount).
   - `greatest_decrease`: To store the greatest decrease in profits (date and amount).

3. **Process Each Row**
   - Iterates through each row in the CSV file.
   - Increments the total month count.
   - Adds to the net total amount of "Profit/Losses".
   - Calculates the monthly changes in "Profit/Losses".
   - Tracks the greatest increase and decrease in profits.

4. **Calculate Results**
   - Calculates the average change in "Profit/Losses".

5. **Print Results**
   - Prints the financial analysis results to the terminal.

6. **Export Results**
   - Exports the results to a text file named `financial_analysis_results.txt`.
