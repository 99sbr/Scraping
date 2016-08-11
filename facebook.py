from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import unittest
import csv
import time
import sys
import simplejson as json
import json
import getpass
from selenium.common.exceptions import NoSuchElementException
###############################################################################
def fix_unicode(data):
    if isinstance(data, bytes):
        return data.encode('utf-8')
    elif isinstance(data, dict):
        data = dict((fix_unicode(k), fix_unicode(data[k])) for k in data);
    elif isinstance(data, list):
        for i in xrange(0, len(data)):
            data[i] = fix_unicode(data[i])
    return data
##############################################################################
def refine(t):
    t=fix_unicode(t)
    tt= t.strip(' \n\t')
    tt=re.sub('\s+',' ',tt)
    tt=tt.replace('\xc2\xa0','')
    return(tt.replace(',',''))
##############################################################################
def check_validation(driver,element_id):
        c=0
        try:
            element = driver.find_element_by_xpath("//a[@title='"+element_id+"']")
            print ("Successfull Login.")
            c=c+1
        except NoSuchElementException:
            c=c
            print( "Not found: %s" % element_id )
        return c
###################################################################
def Scraper(usr,pswd):

    driver=webdriver.Firefox()
    driver.get(base_url)
    username=driver.find_element_by_name('email')
    password=driver.find_element_by_name('pass')
    for j in usr:
        username.send_keys(j)
    for j in pswd:
        password.send_keys(j)
    driver.find_element_by_name('login').click()
    time.sleep(3)
    ######################################checking validation###############################
    element_id='Profile'
    value=check_validation(driver,element_id)
    if (value==1):
        details=[]      # all lists used
        overview=[]
        WorkEdu=[]
        contact=[]
        relationship=[]
        basic_info=[]
        bio=[]
        Family=[]
        other_names=[]
        quotes=[]
        Life_Events=[]
        friends=[]
        noti=[]
        Intro={}     # Dictionary
        About={} 
        Friend_List={}
        Notifications={}
        ##################################### INTRODUCTION ############################################################
        print("Scraping Introduction")
        driver.find_element_by_xpath("//a[@title='Profile']").click()
        time.sleep(2)
        try:
            elements=driver.find_elements_by_xpath("//ul[@id='u_jsonp_2_1v'][@class='uiList _3-8x _2pic _4kg']/li")
            for elm in elements:
                details.append(refine(elm.get_attribute('textContent')))
        except:
            Print("Error in Introduction Section")
        Intro['Introduction']=details
        driver.find_element_by_xpath("//div[@class='_6_7 clearfix']/a[2]").click()
        time.sleep(3)
        ################################# About- overview #############################################################
        print("Scraping overview")
        try:
            elements=driver.find_elements_by_xpath("//ul[@class='uiList _1pi3 _4kg _6-h _703 _4ks']/li")
            for elm in elements:
                overview.append(refine(elm.text))
        except:
            print("Error in overview section")
        About['overview']=overview

        ############ work and Edu #####################################################################################
        print("Scraping work and edu")
        driver.find_element_by_xpath("//li[@title='Work and Education']").click()
        time.sleep(3)
        try:
            elements=driver.find_elements_by_xpath("//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")
            for elm in elements:
                WorkEdu.append(refine(elm.get_attribute('textContent')))
        except:
            print("Error with Work and Education section")
        About['Professional Experience']=WorkEdu
        ############################################ Contact Information ##############################################
        print("Scraping contact details")
        driver.find_element_by_xpath("//li[@title='Contact and Basic Info']").click()
        time.sleep(2)
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_contact']//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")
            for elm in elements:
                contact.append(refine(elm.text))
        except:
            print("Error with Contact section")
        About['Contact info']=contact
        ####################################### Basic Information #####################################################
        print("Scraping basic info")
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_basic']//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")          
            for elm in elements:
                basic_info.append(refine(elm.text))
        except:
            print("Error with Basic info section")

        About['Basic Information']=basic_info
        ####################################### Family and Relationship ###############################################
        print("Scraping family and relationship section")
        driver.find_element_by_xpath("//li[@title='Family and Relationships']").click()
        time.sleep(2)
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_relationships']/div[1]//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")
            for elm in elements:
                relationship.append(refine(elm.text))
        except:
            print("Error with relationship section")
        About['Relationship']=relationship
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_relationships']/div[2]//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")           
            for elm in elements:
                Family.append(refine(elm.text))
        except:
            print("Error with family section")
        About['Family']=Family
        ########################################  Details about you(other names,bio,quotes)#################################################
        driver.find_element_by_xpath("//li[@title='Details About You']").click()
        time.sleep(2)
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_bio']//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")  
            for elm in elements:
                bio.append(refine(elm.text))
        except:
            priint("Error with bio section")
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_nicknames']//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")
            for elm in elements:
                other_names.append(refine(elm.text))
        except:
            print("Error with other names section")
        About['Bio']=bio
        About['Other Names']=other_names
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_quotes']//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")           
            for elm in elements:
                quotes.append(refine(elm.text))
        except:
            print("Error with Quotes section")
        About['Quotes']=quotes

        ########################################  Life Events  #############################################################
        print("Scraping Life_Events")
        driver.find_element_by_xpath("//li[@title='Life Events']").click()
        time.sleep(2)
        try:
            elements=driver.find_elements_by_xpath("//ul[@class='uiList fbProfileEditExperiences _4kg _4ks']/li")       
            for elm in elements:
                Life_Events.append(refine(elm.text))
        except:
            print("Error with Life evens section")
        About['Life Events']=Life_Events
        ##################################### Friend List ###################################################################
        print("Scraping Friend_List")
        driver.find_element_by_xpath("//div[@class='_6_7 clearfix']/a[3]").click()
        time.sleep(3)
        print("Scrolling Down !!")
        for i in range(0,30):
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            elements=driver.find_elements_by_xpath("//div[@id='pagelet_timeline_app_collection_100001976234664:2356318349:2']/ul/li")            
            for elm in elements:
                friends.append(refine(elm.text))

        except:
            print("Error with friends section")

        Friend_List=friends
        ################################################### Notifications ##################################################
        print("Scraping Notifications")
        driver.find_element_by_xpath("//div[@class='_1uh-']/div[3]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='clearfix uiHeaderTop']/div[2]/h3/a").click()
        time.sleep(3)
        print("Scrolling Down")
        for i in range(0,25):
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            elements=driver.find_elements_by_xpath("//div[@class='_44_u']/ul/li")           
            for elm in elements:
                noti.append(refine(elm.text))

        except:
            print("Error with notification section")

        Notifications['Notifications']=noti
        return Notifications,Friend_List,About,Intro
       
    else:
        print("Username or Password Error. Try again")

def Create_JSON(usr,path,Notifications,Friend_List,About,Intro):
        with open("/home/subir_sbr/Desktop/"+usr+"Notifications"+".json", "w") as writeJSON:
                        json.dump(Notifications, writeJSON)
        with open("/home/subir_sbr/Desktop/"+usr+"Friend_List"+".json", "w") as writeJSON:
                        json.dump(Friend_List, writeJSON)
        with open("/home/subir_sbr/Desktop/"+usr+"User_Information"+".json", "w") as writeJSON:
                        json.dump(About, writeJSON)
        with open("/home/subir_sbr/Desktop/"+usr+"User_Introduction"+".json", "w") as writeJSON:
                        json.dump(Intro, writeJSON)

def JSON_Pretty_Print(path):

    with open(path+'User_Introduction.json', 'r') as handle:
        parsed = json.load(handle)
    print(json.dumps(parsed, indent=4, sort_keys=True))

    with open(path+'User_Information.json', 'r') as handle:
        parsed = json.load(handle)
    print(json.dumps(parsed, indent=4, sort_keys=True))

    with open(path+'Friend_List.json', 'r') as handle:
        parsed = json.load(handle)
    print(json.dumps(parsed, indent=4, sort_keys=True))

    with open(path+'Notifications.json', 'r') as handle:
        parsed = json.load(handle)
    print(json.dumps(parsed, indent=4, sort_keys=True))

if __name__ == '__main__':
    path="/home/subir_sbr/Desktop/"         ## set the local path
    base_url="https://www.facebook.com/login/"
    usr = input('Enter Your User Name : ')
    pswd = getpass.getpass(prompt="Enter your password")
    print("Scraping profile. Wait")
    Notifications,Friend_List,About,Intro=Scraper(usr,pswd)
    print("Done !!")
    print("Creating Json")
    Create_JSON(usr,path,Notifications,Friend_List,About,Intro)
    print("Done !!")
    JSON_Pretty_Print(path)
    