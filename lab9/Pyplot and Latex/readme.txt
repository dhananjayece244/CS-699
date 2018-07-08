Pyplot and Latex
Make a report on the previous data assignment in latex. You can chose any other topic also if you wish.

The report can be in single column or two column format and should include:

1) Include your roll number in the author
2) Include sections, subsections, paragraphs
3)  Use different fonts styles and sizes and formatting.
4) Various styles of bullet points ex. itemize, enumerate, etc.
5) Include at least four chart/plot figures generated with pyplot. Each plot should have  different style - line chart, bar chart, histogram etc. From python you will have to save figures.
6) Use float package for proper placing of the figures.  
7) Include at least three complex Mathematical equations of your choice.
8) Include at least one table - you should use python code to generate the table from a dataFrame. The code should write a tex file and your latex file should use '\input' to include that tex file.
9) Use caption for all figures and tables. Use labels for all sections, figures, and, tables. Refer to all figures, tables, and sections in your report using those labels.

Python code for 5) and 8) together will also need to be submitted in a different file.



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


		 
