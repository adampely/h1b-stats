import csv
import sys

def csv2Dict(inputFile, columnNames):
    '''
    This function takes in an input of a csv file to read and the column names to read in from it and returns a list where each item in the list is a dictionary corresponding to one column of the data. Each dictionary contains as keys the unique values of the columns and as the values the number of times that each value appeared (the count).
    
    Inputs:
    inputFile: The string name (with the .csv ending) of the data set that should be read in. This data should be delimited by ";" and the first row of the data should be the column headings. 
    columnNames: a list of the column headings which should be counted into a dictionary.
    
    Outputs:
    dictionaryList: a list of dictionaries where each dictionary corresponds to the count of each unique term in a column. 
    sumItems: The total number of non header rows in the data set (the number of instances in the data set).
    '''
    with open(inputFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        dictionaryList = []  #dictionaryList is a list of dictionaries where each dictioanry represents the keys and counts for each column being counted.
        colIndices =[]   #colIndices will store the index value of the columns which should be counted so they can be accessed in each row of the data.
        try:
            for row in csv_reader:
                #print(row)
                if line_count == 0:
                    
                #The first row must be the column names and will be used to find the appropriate index for the desired list.
                    for columnName in columnNames:
                        #the replace operations below ensure that data from previous years that may have had different column names still works
                        row = [w.replace('JOB_INFO_WORK_STATE','WORKSITE_STATE') for w in row]
                        row = [w.replace('LCA_CASE_WORKLOC1_STATE','WORKSITE_STATE') for w in row]
                        row = [w.replace('PW_SOC_TITLE', 'SOC_NAME') for w in row]
                        row = [w.replace('LCA_CASE_SOC_NAME', 'SOC_NAME') for w in row]
                        headerIndex = row.index(columnName)
                        colIndices.append(headerIndex) #JOB_INFO_WORK_STATE pre-2018
                        dictionaryList.append({})
                    line_count += 1
                else:
                    # A dictionary is made in dictionaryList for each top 10 list that needs to be made.
                    for dictIndex, colIndex in enumerate(colIndices):
                        #The if statement below ensures missing data is ignored, but the line count will still increase (if a string is empty the if statement will be false
                        if row[colIndex]:
                            if row[colIndex] in dictionaryList[dictIndex]:
                                dictionaryList[dictIndex][row[colIndex]] += 1 
                            else:
                                dictionaryList[dictIndex][row[colIndex]] = 1
                    line_count += 1
        except UnicodeDecodeError:
            #There seems to be an error at the end of the larger data sets. This function ignores that error. 
            print('ran into non critical csv read error after ', line_count, ' lines')
            pass
        except Exception as e:
            sys.exit(e)
        sumItems = line_count-1
        return dictionaryList, sumItems