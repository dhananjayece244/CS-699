Data Analysis Assignment
Use the export-import data to answer the following questions. In all the questions use, 2011-12 data by default, unless the question needs data from both years.

Some hints are given but the answer may require much more work than the given hint.
1) Which are are our top five import and export destinations, by total imports and total exports?

2) Which are are our top five import and export commodities?

3) Prepare a single table that shows total imports, total exports, export/import ratio, export-import (trade deficit) for each country. (Hint: use pd.concat)
4) Use the 'query' method to show all countries to whom our export is more than Rs 10,000 Cr. You must use the 'query' method.

5) Save the answer to 4 in a new table. Rename the columns of this table to: 

'Country', 'Exports', 'Imports'

6) Using the table in 5, create a new table with column headings '
Country	Transaction	Value
Hint: use the 'melt' method.

From this table, list our top 10 transactions with various countries. These will be mix of imports and exports.



Country	Transaction	Value
0	U ARAB EMTS	Exports	1.722685e+12
1	U S A	Exports	1.664743e+12


Note: answering 5 or 6 may not be as straightforward as it may appear, depending on how you do it.



7) Make a table of commodities that we both export and import.


Please install xlswriter library if not installed in the system.
Command to install -  sudo pip install xlsxwriter.
Command to run the code:
		a. Open folder in terminal.
		b. Run 'ipython solution.py' in terminal.

Description of code - 

step 1- Import panda library.
		Import xlswriter library.

step 2- Read and parse both the Import and Export xlsx file in two different data frame.

1.a) Calculate total import in year 2011-12 from each country and then sort them in the decreasing 
	 order of total imported value and take top five country. Now write Country column on Q1_imports sheet.

1.b) Calculate total export in year 2011-12 to each country and then sort them in the decreasing 
	 order of total exported value and take top five country and write them on Q1_exports sheet. 

2.a) Calculate total import of each commodities in year 2011-12 and then sort them in the decreasing 
	 order of total imported value and take top five commodities and write them on Q2_imports sheet.

2.b) Calculate total export of each commodities in year 2011-12 and then sort them in the decreasing 
	 order of total exported value and take top five commodities and write them on Q2_exports sheet.

3.   Calculate total import and export of each country and concatinate them on index 'Country'. Add tow
     more column Export/Import and Export-Import and write them on Q3 sheet.

4.   Take data frame of question 3 and take only country whose export value is greater than 10,000Cr using
	 query('Total_exports>1e+11') query operation. And write only 'Country' column on Q4 sheet.

5.   Take data frame of question 3 and take only country whose export value is more than 10,000cr and write 
     country , export and import columns on Q5 sheet.

6.   Take data frame of question 3 and melt total export and total import column and sort them in descending 
	 order and take top 5 country name and transaction and value of transaction and write them on Q6 sheet.

7.  Find those commodities which has been imported in any of the year 2011-12 or 2012-13 by atleast one country 
	and similarly, find those commodities which has been exported by at least one country in the same year and 
	take inner join of both the result and write those commodities on sheet Q7.

Assumptions - 
	Assuming every query is to be done on the basis of 2011-12 data.
	In Q3, After concatination, all NaN has been replaced by 0.
