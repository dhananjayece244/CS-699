1. Command to execute the code :
   Format: python3 solution.py <Village_Name>
   Example:python3 solution.py Agwan

2. Description of Code:
   step-1: I am taking all the available regions in a list.
   step-2: Iterating through each region and getting its jason data.
   step-3: Converting the json data into python object.
   step-4: Looping through each level of multi-level dictionary data and extracting
           the 'key data' and 'value data' and storing them into different lists like 
           District list, taluka list, village list.
   step-5: Checking for the desired village name in the village list. 
   step-6: If village name matches, then storing all its corresponding region,
   		   district, and taluka name in a list.
   step-7: Opening the pdf file in webbrowser and downloading it in temp directory.
   

   
