# h1b-stats
This project creates a top 10 list of the worksite states for H1B visa applications as well as a top 10 list of H1B visa application job classifications. The run.sh can be run in order to start the process. The project run file was designed such that the user could input the desired output attributes relatively easily as input arguments to the run file. 

The src folder contains the source files, which consist of a function that processes the CSV file (csv2Dict.py), a function that sorts dictionaries by value and then alphabetically in case of a tie (sortDictValueAlphabetical.py), and a function that ties the previous two functions together and writes out the top 10 lists (top_10_H1B_lists_2.py). 

The output folder will contain the results from the top_10_H1B_lists_2.py and is currently set to output top_10_occupations.txt and top_10_states.txt. 

It should also be noted that this data set was tested on the ";" seperated data provided by insight on <a href = "https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf" > Google Drive </a>.

# Tests
Test_1: 
The test provided with the problem that ensures correct formatting and output in a simple case. In this case the input data set has less than 10 dictionary entries.

Test_2:
This test ensures that only 10 entries are provided per output file when there are more than 10 available options.

Test_3:
This test ensures that if a data point is missing from an entry, the entry is still counted as an application, but the null value string is not counted as a category that can enter the top 10 list.


SQL answer:
Assuming names of SOCName and State for the two fields, the following are 2 SQL querries that would yield the same lists:

SELECT SOCName 'TOP_OCCUPATIONS', count(SOCName) 'NUMBER_CERTIFIED_APPLICATIONS', ROUND(count(SOCName),3)/(SELECT count(SOCName) FROM h1b_input)*100 'Percentage' FROM h1b_input
GROUP BY SOCName
ORDER BY count(SOCName) DESC, SOCName ASC
LIMIT 10;

SELECT State 'TOP_STATES', count(State) 'NUMBER_CERTIFIED_APPLICATIONS', ROUND(count(State),3)/(SELECT count(State) FROM h1b_input)*100 'Percentage' FROM h1b_input
GROUP BY State
ORDER BY count(State) DESC, State ASC
LIMIT 10;
