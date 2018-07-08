Javascript, JSON, Web API
Your task is to display "Groundwater Recharge Priority Map" for a given village in Maharashtra. The map for all villages in MH is given at https://gsda.maharashtra.gov.in/gwrechargemap.html .

The entire state is divided into various regions, each region having multiple districts. Each district has many talukas and each taluka has multiple villages.

Your program will take a village name on command line. Since there can be multiple villages with same name, it should prepare a list of triples (region, district, taluka) and display them to the user asking them to select the village of interest. For the chosen village, it must obtain the pdf map and display it in a browser.

Notes: 
1. It is critical that you do not download unnecessary files. Make sure that any execution of your program will download only one pdf.

2. Your program should be modular and should use functions.

-----Solution Strategy------

1. Study the source code of start url to understand how data is organized. You will find that it uses javascript and json objects.

2. Figure out the api calls to be made to get the village level data.

3. Get the json data and convert it into python object

4. Iterate over your object to find the villages of interest

5. Once the user selects a village, prepare the corresponding url that wil get you the required map

6. Get the map and save on the disk. Display using webbrowser module.

----Python troubleshooting------

Note that PDF file has to be read as byte-stream, whereas a normal page is read as text-stream. You can use the following code:

def get_data(url, as_bytes=False):
  response = requests.get(url)
  response.raise_for_status()

  if (not as_bytes):
    return response.text
  else: return response.content

The get_data method returns page as text by default.

Remember to provide 'wb' flag when opening the file for writing as binary file.



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
   

   
