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
