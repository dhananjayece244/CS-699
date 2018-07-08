Open project file in terminal.

Command to run :

2.a) First command to run:
     
     python3 figures.py
        

2.c) Second command to run:

	pdflatex -jobname=173050046_report.tex report.tex
	
Brief discription:

After running 2.a) command, five files will get created in the same directory.
Out of five, four would be different chart file(like barchart.pdf, histogram.pdf)
and one would be table.tex. 

After running second command, 173050046_report.pdf file will get created.
Content of this report is one project that I had done during my undergrad.
In this report I have used many Latex properties like section, subsection,
author, title, \textbf, \textit, \underline, \item, and some math function
like \frac{}{}, \int_{}{}, \binom{}{} etc.
To generate different charts, I used  matplotlib.pyplot python package and to 
read input csv file, pandas has been used. To generate line chart, I assumed some 
random data and used in plt.plot() function. After plotting and labeling X and Y
axis, graph has been saved as line.pdf file using plt.savefig() function.
Details of code is written in figures.py file.

Tp generate table.tex file, first I have created a dataframe using random data. And then table.tex file is opend in write mode. After that dataframe has been written into file using dataframe.to_latex() function.

Assumptions:

Used some randome data in plotting histogram and bar charts.
Used hard-coded data in plotting line graph.


		 
