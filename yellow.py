from bs4 import BeautifulSoup
from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
import re
import unittest
import csv
#########################################################################
# cleaning up data and values extracted (HTML parser)
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

#############################################################################

def Create_JSON(driver,popularCategoriesList,popularCategoriesLinkList):		
	Dict={}
	j=0
	for link in popularCategoriesLinkList:
		company=[]
		Address=[]
		Contact=[]
		myDict={}
		print("Getting url: %d\n" % j)
		driver.get(str(link))
		clist=driver.find_elements_by_xpath("//div[@class='serpListDn']/ul/li/div/h2")
		for comp in clist:
			company.append(comp.text)
		addr=driver.find_elements_by_xpath("//div[@class='serpListDn']/ul/li/div/p")
		for a in addr:
			Address.append(a.text)
		cal=driver.find_elements_by_xpath("//div[@class='serpListLft FL']/div[2]")
		for i in cal:
			Contact.append(refine(i.get_attribute('textContent')))
		try:
			for i in range(len(company)):
				myDict[company[i]]=[Address[i],Contact[i]]

		except:
			pass

		Dict[popularCategoriesList[j]]=dict(myDict)
		j=j+1

	with open("/home/subir_sbr/Desktop/"+"YellowPages"+".json", "w") as writeJSON:
	                json.dump(Dict, writeJSON)


#####################################################################################
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)
####################################################################################

def Create_CSV(driver,popularCategoriesList,popularCategoriesLinkList):
	with open('/home/subir_sbr/Desktop/'+'mydata.csv', 'w') as mycsvfile:
		thedatawriter = csv.writer(mycsvfile,dialect='mydialect')
		thedatawriter.writerow(popularCategoriesLinkList)
		
		
######################################################################################
BASE_URL="http://chandigarh.yellowpages.co.in/"
#chromedriver='/home/subir_sbr/SimpliLend/Sbr_Scaping/chromedriver'
driver=webdriver.PhantomJS()
driver.get(BASE_URL)

popularCategoriesList=[]
popularCategoriesLinkList=[]


print("Getting popular category list")
elements=driver.find_elements_by_xpath("//ul[@class='popularCategoriesList']/li")
for ele in elements:
	popularCategoriesList.append(ele.text)
print("popular category list: %s\n" % popularCategoriesList)
print("Getting popular category list links")
elements=driver.find_elements_by_xpath("//ul[@class='popularCategoriesList']/li/h2/a")
for ele in elements:
	popularCategoriesLinkList.append(ele.get_attribute('href'))

print("Creating CSV")
Create_CSV(driver,popularCategoriesList,popularCategoriesLinkList)
print("Creating JSON")
Create_JSON(driver,popularCategoriesList,popularCategoriesLinkList)