Manipulating Excel and CVS files
The Technology and Development Cell at IIT Bombay carries out Design, Evaluation, and Audit of various government schemes for rural development, such as, Jal Yukt Shivar, Thakkar Bapa Adivasi Vikas Yojna etc. During auditing, details of structure being audited are entered into an app, which uploads the data into a cloud service. From the cloud, data is downloaded on a local machine as a CVS file.

The first line of CVS files contains various headers. An example file contains the headers:

'Date', 'Village', 'Habitation', 'Structure', 'Official Work No', 'Length', 'Width', 'Status','Condition','Witness','Picture Link'

But some other work file can contain different headers. All files will contain one heading which has 'work no' as a substring (case-insensitive). While the audit is done per village, audit reports has to be submitted work number wise. 
For this purpose, your program should take a file name (say fff) and a work no (say nnn) on command line. It should open the csv file fff.csv and identify the column that contains 'work no' in its heading. Now it should identify all the rows that contain nnn in the work no column. Each such row should be copied into a separate sheet into an excel file fff_nnn.xlsx (to be created by you). Every sheet in this output file will contain the same headers as the input file, and will contain exactly one additional row corresponding to one occurrence of nnn in work no column in one of the rows in the input file. The sheets will be named nnn_1, nnn_2 etc. Also the work no in each sheet should be changed from nnn to nnn_i .

You should think about various possible errors and handle the errors gracefully by printing informative messages.




1. Command to execute:
	Format:python3 solution.py < input file anme> < work no>
	Working eg-  python3 solution.py student_data 8662006787
2. Description:
 step-1: Reading command line arguments in input_file_name and input_workno.
 step-2: Finding column number of 'input_workno' in the header of input file.
 step-3: Storing all the touples of input file that contains input_work number into a list.
 step-4: Creating sheets to store each touples in different sheets.
 step-5: In each sheet, first row is header information and second row stores the data.
 step-6: Saving the file with desired output file name.


