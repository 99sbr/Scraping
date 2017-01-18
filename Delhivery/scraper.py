from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
import json
import os

BASE_URL='http://www.magicbricks.com/property-for-sale-rent/residential-real-estate?hpr=LINK'

def csv_writer(data, path):
	with open(path, "w",encoding='utf8') as writeJSON: 
		json.dump(data,writeJSON,ensure_ascii=False,sort_keys=True, indent=4)


def open_webpage(script_dir,rel_path,abs_file_path,chromedriver_rel_path):
	abs_file_path = os.path.join(script_dir, rel_path)
	chromedriver_rel_path="Downloads/chromedriver"
	chromedriver=os.path.join(script_dir,chromedriver_rel_path)
	driver=webdriver.Chrome(chromedriver)
	driver.get(BASE_URL)
	return driver

if __name__ == '__main__':
	
	script_dir = os.path.dirname('/home/delhivery/') #<-- absolute dir the script is in
	rel_path = "Desktop/myCityData.json"
	chromedriver_rel_path="Downloads/chromedriver"
	abs_file_path = os.path.join(script_dir, rel_path)
	
	driver=open_webpage(script_dir,rel_path,abs_file_path,chromedriver_rel_path)
	elements=driver.find_elements_by_xpath("//div[@class='w_20_per']")
	cities=[]
	for elm in elements:
		cities.append(elm.get_attribute('textContent').strip(' '))
	City_List={}
	City_List['Cities']=cities
	print(City_List)
	path='/home/delhivery/Desktop/myCityData.json'
	csv_writer(City_List,abs_file_path)
	driver.close()