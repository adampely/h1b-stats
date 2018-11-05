import sys
from csv2Dict import csv2Dict
from sortDictValueAlphabetical import sortDictValueAlphabetical


def top_10_H1B_lists():
    '''
    top_10_H1B_lists
    This function is intended to take an input data file of H1B applications return a top 10 list of the input parameters sorted by number of applications in each category and then alphabetically by the parameter name. The input format is such that the first input argument in the run file is the python file name, then the input file name, and then a pair of column name and desired output file name for a top 10 list for that column. The function is designed to take in any number of column name and file name pairs, but they must be in a format such that goes "COLUMN_NAME1 OUTPUT_NAME1 COLUMN_NAME2 OUTPUT_NAME2"
    
    Inputs:
    All inputs for this function must be from command line variables read in using the sys.argv argument. The order of the aruguments should be [python file name, csv file to be read, a column from the csv file to count, the name of the output file desired, *multiple column name and output file names can be added to the input script*
    '''
    inputArgs = sys.argv[1:]   #The first argv argument seems to be read as the python file name, so it can be discarded.
    numOfArgs = len(inputArgs) #Number of input arguments lets us know how many top 10 lists to make.
    inputFile = inputArgs[0]   #The csv file to be read
    columnNames = inputArgs[1:numOfArgs:2]  #The columns names that will be sorted into top 10 lists.
    outputFileNames = inputArgs[2:numOfArgs:2] #The desired output file names including the .txt extension.
    headerNames = ['TOP_OCCUPATIONS', 'TOP_STATES']  #This is a list of the headings desired for each file name. This could probably be moved out to the argv input arguments.
    
    dictionaryList, sumItems = csv2Dict(inputFile, columnNames)
        
    sortedTop10Lists=[]
    for dataDict in dictionaryList:
        sortedList = sortDictValueAlphabetical(dataDict)
        sortedTop10Lists.append(sortedList[0:10])  #This sorting function sorts first by value of each dictionary key and then alphabetically by the key name. It then keeps only the top 10 values of the sorted list of tuples.

    

    for outputIndex, outputFileName in enumerate(outputFileNames):
        file = open(outputFileName, 'w')
        file.write('{};NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n'.format(headerNames[outputIndex]))
        for sortedTop10List in sortedTop10Lists[outputIndex]:
            file.write('{};{};{:.1f}%\n'.format(sortedTop10List[0], sortedTop10List[1], sortedTop10List[1]/sumItems *100))
        file.close()
    

if __name__ == '__main__':
  top_10_H1B_lists()   
