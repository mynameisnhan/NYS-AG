# NYS-AG
The Office of the New York State Attorney General wanted our group to test 1) whether lawsuit duration could be predicted based on features such as case complexity, municipality, judge, lawyer, motion information, etc. and 2) whether random forest would be a viable model for such a task.

## Dataset
Data was retrieved from the Office of the New York State Attorney General's database and not included for privacy reasons.

## To Run
Go to command prompt

Change directory to project folder

To run, type: python main.py

## Findings
1. Case duration prediction is possible. Our random forest achieved an acceptable R-squared value of 0.7.
2. With the given dataset, only the most important 15 features (feature-engineered using random-forest-based stepwise regression) are needed to achieve an acceptable performance (R-squared = 0.7).
3. Performance stagnated at R-squared = 0.7 after after 15 features.
4. There is a non-linear relationship between case attributes and case length.

## Improvements
DataProc2.py currently takes over 1 week to finish running. Because datetime conversion and subtraction are computationally expensive, a future improvement could be to forego datetime format entirely. 

A possible alternative is that, for each date attribute, we could convert the YMD input to number of days elapsed since the very first day ever recorded in the database (which should be smallest value in "cas1rjidat") and increase our counter with each passing date. Because converting integer to integer is faster than to datetime and because integer math is faster than datetime math, I would expect significant improvement in runtime.

## Notes
Experiments comparing various feature engineering methods, whether to one-hot encode, and alternate regression models were done in Explore.ipynb.
