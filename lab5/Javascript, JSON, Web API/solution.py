#! /bin/python3
import requests
import json
import sys
import webbrowser


#putting all the regions available into a list.
region=["Amravati", "Aurangabad", "Kokan", "Nagpur", "Nashik", "Pune"]
village=sys.argv[1]
k=0;
result = []
#iterating through each region and searching for desired village.
while (k <5):
	url="https://gsda.maharashtra.gov.in/maps/"+region[k]+"/data.js"
	url_data=requests.get(url)
	region_data= json.loads(url_data.text)
	Dist_lists = list(region_data.keys())
	taluka_data= list(region_data.values())
	for i in range(len(Dist_lists)):
		talukas = list(taluka_data[i].keys())
		village_datas = list(taluka_data[i].values())
		for j in range(len(talukas)):
			villages = list(village_datas[j].keys())
			if village in villages:
				q = []
				q.append(region[k])
				q.append(Dist_lists[i])
				q.append(talukas[j])
				result.append(q)
				#print(region[k]," ",Dist_lists[i]," ",talukas[j])
				
				
	k = k+1

#print the list of triplet where this village name exists.
print(result)

my_result = result[0]
region = my_result[0]
district = my_result[1]
taluka = my_result[2]

#Open the file in browser. 
pdf_url="https://gsda.maharashtra.gov.in/maps/"+region+"/"+district+"/"+taluka+"/"+village+".pdf"
webbrowser.open(pdf_url)

#Download the pdf file in current folder.
r = requests.get(pdf_url, stream=True)
with open('/tmp/metadata.pdf', 'wb') as f:
	f.write(r.content)
open('/temp/metadata.pdf','r')

