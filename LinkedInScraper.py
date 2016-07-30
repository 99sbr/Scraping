from bs4 import BeautifulSoup
from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
import re
import unittest
import csv
import time
import sys
import getpass
########################################################
def Get_Profile_Links(driver,Profile_links):
	elements=driver.find_elements_by_xpath("//ol[@id='results']/li/div/h3/a")
	for elm in elements:
		try:
			Profile_links.append(elm.get_attribute('href'))
		except:
			pass
	return Profile_links,driver
	
#########################################################
Name=[]
Profile_links=[]

usr=input("Enter your Email for Linkedin")
pswd=getpass.getpass(promt="Enter your password : ")
base_url="https://www.linkedin.com/uas/login?goback=&trk=hb_signin"
chromedriver='/home/subir_sbr/SimpliLend/Sbr_Scaping/chromedriver'   # path needs to be set
driver = webdriver.Chrome(chromedriver)
driver.get(base_url)
username=driver.find_element_by_name('session_key')
password=driver.find_element_by_name('session_password')
for j in usr:
	username.send_keys(j)
for j in pswd:
	password.send_keys(j)
driver.find_element_by_name('signin').click()
time.sleep(3)
enter=driver.find_element_by_name('keywords')
search="Data scientist,IIT"
for i in search:
	enter.send_keys(i)

driver.find_element_by_xpath("//button[@name='search']").click()
Get_Profile_Links(driver,Profile_links)
COUNT=99
while(len(Profile_links)<=COUNT):
	time.sleep(3)
	driver.find_element_by_xpath("//ul[@class='pagination']/li[@class='next']/a").click()
	Get_Profile_Links(driver,Profile_links)
print(len(Profile_links))
#########################################################################################
def Get_Details(driver,Profile_Url):
	def fix_unicode(data):
	    if isinstance(data, bytes):
	        return data.encode('utf-8')
	    elif isinstance(data, dict):
	        data = dict((fix_unicode(k), fix_unicode(data[k])) for k in data);
	    elif isinstance(data, list):
	        for i in xrange(0, len(data)):
	            data[i] = fix_unicode(data[i])
	    return data 
	def refine(t):
	    t=fix_unicode(t)
	    tt= t.strip(' \n\t')
	    tt=re.sub('\s+',' ',tt)
	    #tt=t.translate(None,'\t\n')
	    tt=tt.replace('\xc2\xa0','')
	    return(tt.replace(',',''))
	#########################################################################
	#Profile_Url="https://www.linkedin.com/in/sbrvrm?trk=nav_responsive_tab_profile"
	#driver=webdriver.PhantomJS()
	#chromedriver='/home/subir_sbr/SimpliLend/Sbr_Scaping/chromedriver'
	#driver = webdriver.Chrome(chromedriver)
	driver.get(Profile_Url)
	FinalList=[]
	######################################
	try:
		Name=driver.find_element_by_xpath("//span[@class='full-name']").text
		print(Name)
	except:
		Name=''
	try:
		Position=driver.find_element_by_xpath("//tr[@id='overview-summary-current']/td/ol/li/span").get_attribute('textContent')
		print(Position)
	except:
		Position=''
	try:
		Previous_Position=driver.find_element_by_xpath("//tr[@id='overview-summary-past']/td").get_attribute('textContent')
	except:
		Previous_Position=''
	
	#Summary=driver.find_element_by_xpath("//div[@class='description']").text
	

	############### PROJECTS ###########################################################
	#Number_of_Projects=driver.find_elements_by_xpath("//section[@id='projects']/ul/li")
	#print("Number of Projects:\n%d" % len(Number_of_Projects))

	Projects=[]
	try:
		elments=driver.find_elements_by_xpath("//section[@id='projects']/ul/li/header/h4")
		for elm in elments:
			Projects.append(refine(elm.text))
	except:
		pass
	####################### PUBLICATIONS ##################################################
	'''Number_of_Publications=driver.find_elements_by_xpath("//section[@id='publications']/ul/li")
	
	elments=driver.find_elements_by_xpath("//section[@id='publications']/ul/li/header/h4")
	for elm in elments:
		Paper_Title.append(refine(elm.text))'''
	############################ SKILLS ######################################################
	Skills=[]
	try:
		elements=driver.find_elements_by_xpath("//div[@id='profile-skills']/ul/li//span[@class='wrap']")
		for elm in elements:
			if elm.text is not None: 
				Skills.append(refine(elm.get_attribute('textContent')))
			else: pass
	except:
		pass

	############################ Experiance ######################################################
	Pos=[]
	try:
		elements=driver.find_elements_by_xpath("//div[@id='background-experience']/div/div/header/h4")
		for elm in elements:
			if elm.text is not None: 
				Pos.append(refine(elm.text))
			else: pass
	except:
		pass
	
	pos = [i for i in pos if i != '']
	Company=[]
	try:
		elements=driver.find_elements_by_xpath("//div[@id='background-experience']/div/div/header/h5")
		for elm in elements:
			if elm.text is not None: 
				Company.append(refine(elm.text))
			else: pass
	except:
		pass
	Company= filter(None,Company)
	Company = [i for i in Company if i != '']
	Experience={}
	try:
		for i in range(len(Position)):
			myDict={}
			myDict['Position']=Position[i]
			myDict['Company Name']=Company[i]
			Experience[i]=dict(myDict)
	except:
		pass

	########################### Education ########################################################
	Education=[]
	try:
		elments=driver.find_elements_by_xpath("//div[@id='background-education']/div/div/div/header/h4/a")
		for elm in elments:
			Education.append(refine(elm.text))
	except:
		pass
	print(Education)
	Education = [i for i in Education if i != '']

	FinalList.append(Name)
	FinalList.append(Position)
	FinalList.append(Previous_Position)
	FinalList.append(Education)
	FinalList.append(Experience)
	FinalList.append(Skills)
	FinalList.append(Projects)
	return FinalList

##########################################################################
import csv
arrayofdata=[]
for i in range(0,len(Profile_links)):
	arrayofdata.append(Get_Details(driver,Profile_links[i]))

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)             
with open('/home/subir_sbr/Desktop/'+'mydata.csv', 'w') as mycsvfile:     # set the path for csv file
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for row in arrayofdata:
        thedatawriter.writerow(row)

driver.close()