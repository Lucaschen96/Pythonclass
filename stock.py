import csv
import os

for file in os.listdir('data'):
    line_count = 0
    data = []
    if file.endswith('.csv'):
        filepath='data/' + file
        with open(filepath, 'r') as csvreader:
            reader = csv.reader(csvreader)
            for row in reader:
                if line_count == 0:
                    line_count += 1
                    row.append('percentage change')
                    data.append(row)
                    continue
                change = (float(row[4]) - float(row[1])) / float(row[1]) * 100
                row.append(change)
                data.append(row)

        with open(filepath, 'w') as csvwriter:
            writer = csv.writer(csvwriter)
            for row in data:
                writer.writerow(row)







