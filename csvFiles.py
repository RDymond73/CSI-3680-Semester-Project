import csv, os

def readCSV():
# Get only csv files.
    for csvFilename in os.listdir('.'): 
        if not csvFilename.endswith('.csv'):
            continue # skip non-csv files 
        
    with open(csvFilename, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            print(row)

readCSV()