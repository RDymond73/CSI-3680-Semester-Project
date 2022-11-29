from htmlTemplate import *
from csvFiles2 import *

test = [['Rick Dymond', '11/10/99', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5'], ['Rick Dymond', '11/10/99', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5'], ['Rick Dymond', '11/10/99', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5']]


def master():
    #create folder for html pages
    createFolder()
    # get data from csv file
    data = readCSV()
    #create html page for data
    
    i = 4
    while i > 0:
        createHTML(data[i])
        i = i - 1
        continue

master()
