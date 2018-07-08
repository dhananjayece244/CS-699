import os,re
#function to extract email id from input file and write them back on the output file with #masked email id.
def extract_email():
	#opening input and output files
	input_file = open('input.txt','r')
	output_file = open('output.txt','w')

	#scanning input text file line by line and extracting email-id.
	for line in input_file:
		email=re.search(r'[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+[.]\w{2,3}',line)
		mid  =re.search(r'[a-zA-Z0-9_.]+@',line)
		ind_mob=re.search(r'\+91\d{10}',line)
		pak_mob=re.search(r'\+92\d{10}',line)
		us_ph = re.search(r'\+1\d{10}',line)
		date = re.search(r'([012][0-9]|[3][01])[-]([0][0-9]|[1][[012])[-]\d{4}',line)
		
		time =re.search(r'([01][0-9]|[2][0-3])[:]([0-5][0-9])[:]([0-5][0-9])',line)
		subnet_id=re.search(r'([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\s([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\s([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\s([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])',line)
		
		
		temp=line
		
		if subnet_id:
			temp=re.sub(r'([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\s([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\s([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\s([01][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])','qqq xxx yyy zzz',temp)

		
		if time:
			temp=re.sub(r'([01][0-9]|[2][0-3])[:]([0-5][0-9])[:]([0-5][0-9])','hh:mm:ss',temp)
		if date:
			temp=re.sub(r'([012][0-9]|[3][01])[-]([0][0-9]|[1][[012])[-]\d{4}','dd-mm-yyyy',temp)
		if email:
		    temp=re.sub(r'[a-zA-Z0-9_.]+@','#'*(len(mid.group())-1)+'@',temp)	
		if ind_mob:
		    temp=re.sub(r'\+91\d{10}','+91'+'*'*10,temp)
		if pak_mob:
		    temp=re.sub(r'\+92\d{10}','+92'+'*'*10,temp)	
		if us_ph:
		    temp=re.sub(r'\+1\d{10}','+1'+'*'*10,temp)	
			
		output_file.write(temp)

	#closing files
	input_file.close()
	output_file.close()

#function to extract Indian phone number from input file and write them back on the output file with masked phone number.	
'''
def extract_Indian_phone():
	#opening output files
	input_file = open('output.txt','r+')
	

	#scanning input text file line by line and extracting Indian phone number.
	for line in input_file:
		ind_mob=re.search(r'\+91\d{10}',line)
		temp=line
		if ind_mob:
		    temp=re.sub(r'\+91\d{10}','+91'+'*'*10,temp)	
		input_file.write(temp)

	#closing files
	input_file.close()

#function to extract phone number of Pakistan from input file and write them back on the output file with masked phone number.	
def extract_Pak_phone():
	#output files
	input_file = open('output.txt','r+')
	

	#scanning input text file line by line and extracting phone number of Pakistan.
	for line in input_file:
		pak_mob=re.search(r'\+92\d{10}',line)
		temp=line
		if pak_mob:
		    temp=re.sub(r'\+92\d{10}','+92'+'*'*10,temp)	
		input_file.write(temp)

	#closing files
	input_file.close()

	

#function to extract phone number of USA from input file and write them back on the output file with masked phone number.
def extract_us_phone():
	#opening last updated output file.
	input_file = open('output.txt','r+')
	

	#scanning input text file line by line and extracting phone number of USA.
	for line in input_file:
		us_ph = re.search(r'\+1\d{10}',line)
		temp=line
		if us_ph:
		    temp=re.sub(r'\+1\d{10}','+1'+'*'*10,temp)	
		input_file.write(temp)

	#closing files
	input_file.close()

'''
#function to print number of Indian mobile number and total number of email ids.

def statistical_summary():
	count=0
	email=0
	input_file=open('input.txt','r')
	
	for line in input_file:
		count = count + line.count('+91')
		email=email+line.count('@')
		
	print(" Number of Indian mobile number = " , count)
	
	print(" Number of Email ids  = " , email)
    
   
	input_file.close()

extract_email()
statistical_summary()

 
