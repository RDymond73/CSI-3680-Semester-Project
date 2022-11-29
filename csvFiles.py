import csv, os

def readCSV():
    data = [] 
# Get only csv files.
    for csvFilename in os.listdir('.'): 
        if not csvFilename.endswith('.csv'):
            continue # skip non-csv files 
        
    with open(csvFilename, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            for cell in row:
                # print(row)
                data.append(row)
                print(data)
            


readCSV()