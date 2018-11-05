def sortDictValueAlphabetical(dataDict):
    '''
    sortDictValueAlphabetical
    This function in intended to take in a dictionary with values that are integers and sort it in descending order first by the value of the dictionary and in the case of a tie then in alphabetical order.
    
    inputs:
    dataDict: A dictionary with values that are integers and keys that can be strings or integers
    
    outputs:
    sortedList: a list of tuples with the tuples going in the order of (key,value) and the list going in descending order of value with ties broken by alphabetical value of key. 
    '''
    sortedList = [v for v in sorted(dataDict.items(), key=lambda kv: (-kv[1], kv[0]))]
    
    return sortedList