import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# with open(csvpath) as csvfile:
    
#     csvreader = csv.reader(csvfile, delimiter = ",")

#     print(csvreader)

#     csv_header = next(csvreader)

#     print(f"CSV Header: {csv_header}")

#     # Read each row of data after the header
#     for row in csvreader:
#         print(row)

print ("----------------------------")

# count = 0
# with open(csvpath) as csvfile:
    
#     csvreader = csv.reader(csvfile, delimiter = ",")
#     next(csvreader)
#     for row in csvreader:
#         count = count + 1
#     print(int(count))

print ("----------------------------")

# total = 0
# with open(csvpath) as csvfile:
    
#     csvreader = csv.reader(csvfile, delimiter = ",")
#     next(csvreader)
#     for row in csvreader:
#         total = total + int(row[1])
    
#     print(total)

print ("----------------------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    first_row = next(csvreader)
    prev_row = int(first_row[1])
    net_change = 0

    for row in csvreader:
        net_change = int(row[1]) - prev_row
        prev_row = int(row[1])
        print(net_change)

