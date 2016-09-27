from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
import simplejson as json
import json
import getpass
from selenium.common.exceptions import NoSuchElementException
import numpy as np
import collections
from collections import OrderedDict
import string
import io
##################################################################

def Get_Data(base_url,city,username,gender,value):		# Extracts table data
	driver=webdriver.PhantomJS()
	driver.get(base_url)
	driver.find_element_by_xpath("//select[@id='ddlDistricts']//option[@value='"+city+"']").click()
	time.sleep(2)
	driver.find_element_by_id('RdlSearchBy_1')
	driver.find_element_by_xpath("//input[@id='RdlSearchBy_1']").click()
	name=driver.find_element_by_id('txtFirstName')
	#username=input("Enter the name character:\n")
	for char in username:
		name.send_keys(char)

	driver.find_element_by_xpath("//select[@id='ddlGender']//option[@value='"+gender+"']").click()
	driver.find_element_by_id('Button1').click()
	time.sleep(1)
	elements=driver.find_elements_by_xpath("//table[@id='gvSearchResult']/tbody/tr/th")
	Column_Names=[]
	for elm in elements:
		Column_Names.append(elm.text)
	Column_Names=Column_Names[5:11]
	List=[]
	Link_List=[]
	
	Record={}
	links=driver.find_elements_by_xpath("//table[@id='gvSearchResult']/tbody/tr/td//table/tbody/tr/td/a")
	for link in links:
		Link_List.append(link.get_attribute('href'))
	
	elements=driver.find_elements_by_xpath("//table[@id='gvSearchResult']/tbody/tr")
	for elm in elements:
		List.append(elm.find_elements_by_tag_name("td")[5:11])
	for i in List:
		for j in i:
			value.append(j.text)
	driver.close()


def Crawl_City(city):		# records the data in suitable format by transforming and saving in JSON format
	path="/home/subir_sbr/Desktop/"         ## set the local path
	char=list(string.ascii_lowercase)
	gender=['M','F','O']		# Gender O stands for TransGender
	value=[]
	base_url="http://164.100.180.82/searchengine/SearchEngineEnglish.aspx"

	for g in gender:
		for c in char:
			print("Extracting Details for name with char %s of gender %s"% (c,g))
			Get_Data(base_url,city,c,g,value)	# getting data for different gender and name character
			print(len(value))

	Column_Names=['First Name', 'Name (Hindi)', "Father/Husband's Name", "Father/Husband's Name (Hindi)", 'Age', 'Gender']	
	myarray=np.asarray(value)
	m=len(myarray)
	n=len(Column_Names)
	myarray.resize(m/n,n)
	details =myarray.tolist()
	CompleteDict={}
	Record={}
	finalDict={}
	CompleteDict=collections.OrderedDict(CompleteDict)
	Record=collections.OrderedDict(Record)
    
	for i in range(len(details)):
		for j in range(len(Column_Names)):
			Record[Column_Names[j]]=details[i][j]
		CompleteDict[i]=dict(Record)	# final dictionay having all the data

	with open("/home/subir_sbr/Desktop/"+city+".json", "w",encoding='utf8') as writeJSON: 	#path of
		json.dump(CompleteDict,writeJSON,ensure_ascii=False,sort_keys=True, indent=4)


if __name__ == '__main__':

	Crawl_City("08")	# for agra
	Crawl_City("09")	# for aligarh

   
   