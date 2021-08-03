# Database Search

## Description
This is a command line application in Python. Each module conducts search on one of three (3) databases, each a .json file. The results are displayed on the screen in a clear format. A search command returns values from all related entities. For example, when a user searches the key “timezone” and the value “Sri Lanka,” the output is a display of keys and values for each set of data that contains “Sri Lanka” for “timezone.”

## Modules
1.	Search_Organizations.py
2.	Search_Tickets.py
3.	Search_Users.py

## Testing Modules
1. Test_Search_Organizations.py
2. Test_Search_Tickets.py
3. Test_Search_Users.py

## Test Results
The tests determine whether the program can read all data types contained within each database:
1.	string
2.	integer
3.	boolean
4.	list
<p>All tests produce satisfactory results.

## Technologies
1. Python’s json library
2. Python’s unittest library

## Execution
From the Main folder, run `main.py`

## Notes
In this program, the Boolean true and false in the .json files did not properly convert to True and False in Python. My program still works but in the next iteration I will fix this issue. Another issue that needs to be worked on in the next iteration is accounting for Null or None values.
