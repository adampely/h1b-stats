# h1b-stats
This project creates a top 10 list of the worsite states for H1B visa applications as well as a top 10 list of H1B visa application job classifications. The run.sh can be run in order to start the process. The project run file was designed such that the user could could the desired output attributes relatively easily as input arguments to the run file. 

The src folder contains the source files, which consist of a function that processes the CSV file (csv2Dict.py), a function that sorts dictionaries by value and then alphabetically in case of a tie (sortDictValueAlphabetical.py), and a function that ties the previous two functions together and writes out the top 10 lists (top_10_H1B_lists_2.py). 

The output folder will contain the results from the top_10_H1B_lists_2.py and is currently set to output top_10_occupations.txt and top_10_states.txt. 

# Tests
Test_1: 
The test provided with the problem that ensures correct formatting and output in a simple case. In this case the input data set has less than 10 dictionary entries.

Test_2:
This test ensures that only 10 entries are provided per output file when there are more than 10 available options.

Test_3:
This test ensures that if a data point is missing from an entry, the entry is still counted as an application, but the null value string is not counted as a category that can enter the top 10 list.
