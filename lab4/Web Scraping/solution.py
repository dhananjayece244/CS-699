import sys
import getpass;
import re;
import requests

import re;
import bs4;
from collections import Counter

def start_moodle_session(user,passwd):
  login_url="http://moodle.iitb.ac.in/login/index.php"
  #user=input('username:')
  #passwd=getpass.getpass()

  session=requests.session()
  
  
  result=session.post(login_url, data={'username':user,'password':passwd})
  if result.status_code != 200:
    print ("Error status", result.status_code, "when logging", login_url)

  return session


def get_page(url, session):
  result = session.get(url)
  if result.status_code != 200:
    print ("Error status", result.status_code, "when fetching", url)

  content=bs4.BeautifulSoup(result.text,'html.parser')

  return content
  


#login and get my moodle landing page
start_url ="http://moodle.iitb.ac.in/my"

def main(argv):
    user=sys.argv[1]
    paswd=sys.argv[2]
    session = start_moodle_session(user,paswd)

    # find the url for course on landing page
    content = get_page(start_url, session)
    for c in content.findAll("div",{"class":"course_title"}):
    	if c.text[:6]=="CS 699":
    		course_page=c.find('a')['href']
    
    #find the url for News Forum. 
 
    lab_page=get_page(course_page,session)
    for l in lab_page.findAll("div",{"class":"activityinstance"}):
    	if l.text[:10]=="News forum":
    		news_link=l.find('a')['href']
    
    #find the count of a pattern inside each discussion thread
    
    discuss_page=get_page(news_link,session) 
    for link in discuss_page.findAll("td",{"class":"topic starter"}):
    	print (link.text)
    	dis_thread=get_page(link.find('a')['href'], session)
    	count=0;
    	for t in dis_thread.findAll("div",{"class":"content"}):
    		content=t.prettify()
    		temp=sum('+1' == line.strip() for line in content.split('\n'))		
    		count = count + temp
    	
    	print (count)
    	
    return 

if __name__ == "__main__":
    main(sys.argv)

