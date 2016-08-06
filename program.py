import pandas as pd
import csv
import re
business_services = pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=0)
Trading = pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=1)
ElecGasWater= pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=2)
Manufacturing = pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=3)
Agriculture = pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=4)
Manufacturing_food = pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=5)
Manufacturing_Machines = pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=6)
Manufacturing_ppr = pd.read_excel(open('/home/subir_sbr/Desktop/Xeler8/keywords-Testing.xlsx','rb'), sheetname=7)

Data=pd.read_csv('/home/subir_sbr/Desktop/Xeler8/CompaniesInfo-Testing.csv',encoding = "ISO-8859-1")
df=pd.DataFrame(Data)
Company_Name=Data['COMPANY NAME']
Activity=Data.ACTIVITY_DESCRIPTION
def filtereOuput(company,activity):       # this function creates the filtere Output file
    flag=[]
    company=str(company)
    activity=str(activity)
    
    for i in range(len(business_services)):
        s=str(business_services.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(Trading)):
        s=str(Trading.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(ElecGasWater)):
        s=str(ElecGasWater.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(Manufacturing)):
        s=str(Manufacturing.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(Agriculture)):
        s=str(Agriculture.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(Manufacturing_food)):
        s=str(Manufacturing_food.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(Manufacturing_Machines)):
        s=str(Manufacturing_Machines.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(Manufacturing_ppr)):
        s=str(Manufacturing_ppr.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)         
    return flag  
#################################################
def Business_Services(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(business_services)):
        s=str(business_services.at[i,'Keywords'])
        
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    
    return flag
################################################
def Trading_Tag(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(Trading)):
        s=str(Trading.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    
    return flag
################################################
def ECW(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(ElecGasWater)):
        s=str(ElecGasWater.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    
    return flag
################################################
def Manufacturing_Tag(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(Manufacturing)):
        s=str(Manufacturing.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    
    return flag
################################################
def Agriculture_Tag(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(Agriculture)):
        s=str(Agriculture.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    
    return flag
################################################
def Food_Manufacturing(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(Manufacturing_food)):
        s=str(Manufacturing_food.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    
    return flag
################################################
def Machine_Manufacturing(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(Manufacturing_Machines)):
        s=str(Manufacturing_Machines.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
    
    return flag
################################################
def Paper_Manufacturing(company,activity):
    flag=[]
    company=str(company)
    activity=str(activity)
    for i in range(len(Manufacturing_ppr)):
        s=str(Manufacturing_ppr.at[i,'Keywords'])
        if re.match(".*"+s+".*",company,flags=re.I) or re.match(".*"+s,company,flags=re.I) or re.match(s+".*",company,flags=re.I) or re.match(".*"+s+".*",activity,flags=re.I) or re.match(".*"+s,activity,flags=re.I) or re.match(s+".*",activity,flags=re.I):
            flag.append(1)
        else:
            flag.append(0)
           
    return flag    
###############################################
file= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput.csv', 'w')
write= csv.writer(file)
print("filter output file creation in process please wait....")
for i in range(len(df)):
    if any(filtereOuput(Company_Name[i],Activity[i]))==1:       
        write.writerows([df.ix[i]])
file.close()

print("filtere Output has been created !!!")
#######################################################################################################
filtereData=pd.read_csv('/home/subir_sbr/Desktop/Xeler8/CompaniesInfo-Testing.csv',encoding = "ISO-8859-1")
frame=pd.DataFrame(filtereData)
filteredCompany=frame['COMPANY NAME']
filteredActivity=frame.ACTIVITY_DESCRIPTION

file1= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_businessServices.csv', 'w')
write1= csv.writer(file1)
print("business services file is being created....")
for i in range(len(frame)):
    if any(Business_Services(filteredCompany[i],filteredActivity[i]))==1:        
        write1.writerows([frame.ix[i]])
file1.close()
print("Done")
########################################################################################################
file2= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_Trading.csv', 'w')
write2= csv.writer(file2)
print("Trading file is being created....")
for i in range(len(frame)):
    if any(Trading_Tag(filteredCompany[i],filteredActivity[i]))==1:
        write2.writerows([frame.ix[i]])
file2.close()
print("Done")
########################################################################################################
file3= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_ECW.csv', 'w')
write3= csv.writer(file3)
print("ECW file is being created....")
for i in range(len(frame)):
    if any(ECW(filteredCompany[i],filteredActivity[i]))==1:
        write3.writerows([frame.ix[i]])
file3.close()
print("Done")
########################################################################################################
file4= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_Manufacturing_Tag.csv', 'w')
write4= csv.writer(file4)
print("Manufacturing file is being created....")
for i in range(len(frame)):
    if any(Manufacturing_Tag(filteredCompany[i],filteredActivity[i]))==1:
        write4.writerows([frame.ix[i]])
file4.close()
print("Done")
########################################################################################################
file5= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_Agriculture_Tag.csv', 'w')
write5= csv.writer(file5)
print("Agriculture file is being created....")
for i in range(len(frame)):
    if any(Agriculture_Tag(filteredCompany[i],filteredActivity[i]))==1:
        write5.writerows([frame.ix[i]])
file5.close()
print("Done")
########################################################################################################
file6= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_Food_Manufacturing.csv', 'w')
write6= csv.writer(file6)
print("Food Manufacturing file is being created....")
for i in range(len(frame)):
    if any(Food_Manufacturing(filteredCompany[i],filteredActivity[i]))==1:
        write6.writerows([frame.ix[i]])
file6.close()
print("Done")
########################################################################################################
file7= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_Machine_Manufacturing.csv', 'w')
write7= csv.writer(file7)
print("Machine Manufacturing file is being created....")
for i in range(len(frame)):
    if any(Machine_Manufacturing(filteredCompany[i],filteredActivity[i]))==1:
        write7.writerows([frame.ix[i]])
file7.close()
print("Done")
########################################################################################################
file8= open('/home/subir_sbr/Desktop/Xeler8/filtereOuput_Paper_Manufacturing.csv', 'w')
write8= csv.writer(file8)
print(" Paper Manufacturing file is being created....")
for i in range(len(frame)):
    if any(Paper_Manufacturing(filteredCompany[i],filteredActivity[i]))==1:
        write8.writerows([frame.ix[i]])
file8.close()
print("DOne")
########################################################################################################