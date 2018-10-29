# NYS-AG
Goal: Predicting duration of lawsuit based on features such as case complexity, municipality, judge, lawyer, motion information, etc.

## Dataset
Dataset was retrieved from the Office of the NY State Attorney General's database and not included for privacy reasons.

## To Run
Go to command prompt
Change directory to project folder
To run, type: python main.py

## Improvements
DataProc2.py currently takes over 1 week to finish running. Because datetime conversion and subtraction are computationally expensive, a future improvement could be to forego datetime format entirely. Instead, for each date attribute, we could convert the YMD input to number of days elapsed since the very first day ever recorded in the database (which should be smallest value in "cas1rjidat") and increase our counter with each passing date. Because converting integer to integer is faster than to datetime and because integer math is faster than datetime math, I would expect significant improvement in runtime.
