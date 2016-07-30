from bs4 import BeautifulSoup
from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
import re
import unittest
import csv
#########################################################################
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
Profile_Url="https://www.linkedin.com/in/sbrvrm?trk=nav_responsive_tab_profile"
#driver=webdriver.PhantomJS()
chromedriver='/home/subir_sbr/SimpliLend/Sbr_Scaping/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get(Profile_Url)

######################################
Name=driver.find_element_by_xpath("//h1[@id='name'][@class='fn']").text
print("Name of User :\n%s " % Name)
Position=driver.find_element_by_css_selector('p.headline.title').text
print("Position of User :\n%s " % Position)
Previous_Position=driver.find_element_by_xpath("//table[@class='extra-info']/tbody/tr[2]/td").text
print("Previous Position of User :\n%s " % Previous_Position)
Education=driver.find_element_by_xpath("//table[@class='extra-info']/tbody/tr[3]/td").text
print("Education of User :\n%s " % Education)
Summary=driver.find_element_by_xpath("//div[@class='description']").text
print("Summary of User:\n%s" % Summary)

############### PROJECTS ###########################################################
Number_of_Projects=driver.find_elements_by_xpath("//section[@id='projects']/ul/li")
print("Number of Projects:\n%d" % len(Number_of_Projects))

Headers=[]
elments=driver.find_elements_by_xpath("//section[@id='projects']/ul/li/header/h4")
for elm in elments:
	Headers.append(refine(elm.text))


Descripion=[]
elments=driver.find_elements_by_xpath("//section[@id='projects']/ul/li/p")
for elm in elments:
	Descripion.append(refine(elm.text))



Contributors=[]
elments=driver.find_elements_by_xpath("//section[@id='projects']/ul/li/dl/dd")
for elm in elments:
	Contributors.append(refine(elm.text))


Project={}
for i in range(len(Headers)):
	myDict={}
	myDict['Topic']=Headers[i]
	myDict['Description']=Descripion[i]
	myDict['Contributors']=Contributors[i]
	Project[i]=dict(myDict)

#print("Complete Project Details: \n %s" % Project)

####################### PUBLICATIONS ##################################################
Number_of_Publications=driver.find_elements_by_xpath("//section[@id='publications']/ul/li")
print("Number of Publications:\n%d" % len(Number_of_Publications))


Publication_House=[]
elments=driver.find_elements_by_xpath("//section[@id='publications']/ul/li/header/h5")
for elm in elments:
	Publication_House.append(refine(elm.text))

Paper_Title=[]
elments=driver.find_elements_by_xpath("//section[@id='publications']/ul/li/header/h4")
for elm in elments:
	Paper_Title.append(refine(elm.text))

Authors=[]
elments=driver.find_elements_by_xpath("//section[@id='publications']/ul/li/dl/dd")
for elm in elments:
	Authors.append(refine(elm.text))

Publications={}
for i in range(len(Publication_House)):
	myDict={}
	myDict['Publication House']=Publication_House[i]
	myDict['Papaer Title ']=Paper_Title[i]
	myDict['Authors']=Authors[i]
	Publications[i]=dict(myDict)

print("Complete publication Details: \n %s" % Publications)


############################ SKILLS ######################################################
Skills=[]
elements=driver.find_elements_by_xpath("//section[@id='skills']/ul/li//span[@class='wrap']")
for elm in elements:
	if elm.text is not None: 
		Skills.append(refine(elm.get_attribute('textContent')))
	else: pass
print("Skills of user: \n%s" % Skills)

############################ Experiance ######################################################
Position=[]
elements=driver.find_elements_by_xpath("//section[@id='experience']/ul/li/header/h4")
for elm in elements:
	if elm.text is not None: 
		Position.append(refine(elm.text))
	else: pass

Company=[]
elements=driver.find_elements_by_xpath("//section[@id='experience']/ul/li/header/h5")
for elm in elements:
	if elm.text is not None: 
		Company.append(refine(elm.text))
	else: pass

Experience={}
for i in range(len(Position)):
	myDict={}
	myDict['Position']=Position[i]
	myDict['Company Name']=Company[i]
	Experience[i]=dict(myDict)
print("Experiance of user: \n%s"% Experience)

########################### COURSES ########################################################
Courses=[]
elments=driver.find_elements_by_xpath("//section[@id='courses']/ul/li/div/ul/li")
for elm in elments:
	Courses.append(refine(elm.text))

FinalList=[Name,Position,Previous_Position,Education,Project,Paper_Title,Skills,Courses,Experience]
driver.close()
Csv_List=[]
Csv_List.append(FinalList)
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)             
with open('/home/subir_sbr/Desktop/'+'mydata.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for row in Csv_List:
        thedatawriter.writerow(row)










