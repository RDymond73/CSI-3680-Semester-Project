import csv
#import pandas as pd
import os
import glob


def readCSV():
    dataCSV = []
# Get only csv files.
    for csvFilename in os.listdir('.'): 
        if not csvFilename.endswith('.csv'):
            continue # skip non-csv files 
        
        with open(csvFilename, 'r') as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                dataRow = []
                # print(row)
                for cell in row:
                    #  print(cell)
                     dataRow.append(cell)
                dataCSV.append(dataRow)
            print(dataCSV)
            return dataCSV

def getRowNum():
    for csvFilename in os.listdir('.'): 
        if not csvFilename.endswith('.csv'):
            continue # skip non-csv files 
        with open(csvFilename, 'r') as file:
            csvReader = csv.reader(file)
            counterRow = 0
            for row in csvReader:
                counterRow = counterRow + 1
            #print(counterRow)
            return counterRow - 1
            


#readCSV()
#getRowNum()

# Using glob
#path = os.getcwd()
#csv_files = glob.glob(os.path.join(path, "*.csv"))
    
# loop over the list of csv files
#for f in csv_files:
      
    # read the csv file
#    df = pd.read_csv(f)
      
    # print the location and filename
#    print('Location:', f)
#    print('File Name:', f.split("\\")[-1])
      
    # print the content
#    print('Content:')
#    print(df)