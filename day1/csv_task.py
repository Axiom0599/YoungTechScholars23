import csv

file1 = open("filecsv.csv", 'w')
csv_writer = csv.writer(file1)
csv_writer.writerow(['hello','world'])
