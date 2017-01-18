from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
import json
import scraper as sc
import os
import time
BASE_URL='http://www.magicbricks.com/property-for-sale-rent/residential-real-estate?hpr=LINK'

if __name__ == '__main__':
	script_dir = os.path.dirname('/home/delhivery/') #<-- absolute dir the script is in
	rel_path = "Desktop/myCityData.json"
	chromedriver_rel_path="Downloads/chromedriver"
	abs_file_path = os.path.join(script_dir, rel_path)

	driver=sc.open_webpage(script_dir,rel_path,abs_file_path,chromedriver_rel_path)
	with open(abs_file_path) as data_file:
		data = json.load(data_file)
	city_name_field=driver.find_element_by_xpath("//input[@id='keyword']")
	driver.find_element_by_id('rentTab').click()
	for characters in data['Cities'][0]:
		city_name_field.send_keys(characters)
	
	driver.find_element_by_xpath("//div[@id='searchWrap']/div[2]/div[1]/span[@class='propertyTypeArrow toggleProList']").click()
	driver.find_element_by_xpath("//input[@type='checkbox'][@title='Flat']").click()
	time.sleep(3)
	driver.find_element_by_xpath("//input[@type='submit']").click()
	




localityIdArray=*
callType=ajax
city=2951
currHeatMapVal=Price+Per+sqft
radius

