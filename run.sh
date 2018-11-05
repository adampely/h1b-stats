#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
#python ./src/testScript2.py ./input/h1b_input.csv SOC_NAME top_10_occupations.txt WORKSITE_STATE top_10_states.txt
python3 ./src/top_10_H1B_lists_2.py ./input/h1b_input.csv SOC_NAME ./output/top_10_occupations.txt WORKSITE_STATE ./output/top_10_states.txt
