import requests
import csv
with open('Gurgaon.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['City','Sector','Polygon','Center-Lat','Center-Lng','Area','Area-Type','Area-Unit','Price'])
with open('Gurgaon.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['Gurgaon','','','','','','','',''])
for j in  range(1,100):
  try:
    Sector=j
    keyword='Sector-'+str(j)+' '+'Gurgaon'
    print('Getting details for %s'% keyword)
    url = "http://www.99acres.com/do/mapsearch/getMapBoundsIntent"

    payload = { 'Refine_Localities':'Refine Localities',
    'action':'/do/quicksearch/search',
    'area_max':'',
    'area_min':'',
    'area_unit':'1',
    'availability':'',
    'budget_max':'',
    'budget_min':'',
    'city':'8',
    'class':'',
    'fullSelectedSuggestions':'',
    'isvoicesearch':'N',
    'keyword':keyword,
    'keyword_suggest':''
    ,'lstAcn':''
    ,'lstAcnId':''
    ,'mapsearch':'1'
    ,'preference':'L'
    ,'property_type[]':'C'
    ,'refine_results':'Y'
    ,'res_com':'C'
    ,'search_location':'SH'
    ,'search_type':'QS'
    ,'searchform':'1'
    ,'selected_tab':'5'
    ,'src':'CLUSTER'
    ,'strEntityMap':""
    ,'texttypedtillsuggestion':''
    }
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "0b825501-da8a-5dc2-ea1d-df261ccd348a"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    d={}
    d=response.json()
    Polygon=[]
    for i in range(len(d['bounds'])):
      Polygon.append(d['bounds'][i])
    


    loc_array=d['intent']['locality_array']
    lat=d['center']['lat']
    lng=d['center']['lng']
    import requests

    url = "http://www.99acres.com/do/mapsearch/getResults_ajax"

    payload = {
        'Refine_Localities':'Refine Localities'
    ,'action':'/do/quicksearch/search'

    ,'area_unit':'1'

    ,'city':'8'
    ,'isvoicesearch':'N'

    ,'locality_array[]':loc_array
    ,'mapsearch':'1'
    ,'preference':'L'
    ,'property_type[]':'C'
    ,'refine_results':'Y'
    ,'res_com':'C'
    ,'search_location':'SH'
    ,'search_type':'QS'
    ,'searchform':'1'
    ,'selected_tab':'5'

     ,   'latitude':lat
    ,'latlongsearch':'1'
    ,'latlongsearchdistance':'1.5'

    ,'longitude':lng
        
    }
    headers = {
        'accept': "*/*",
        'origin': "http://www.99acres.com",
        'x-devtools-emulate-network-conditions-client-id': "1dc2f3f1-b803-434f-bc5e-8de717147a57",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'referer': "http://www.99acres.com/rent-map-view-commercial-property-in-sector-45-gurgaon-ffid?orig_property_type=C&search_type=QS&search_location=SH&lstacn=VSP&pageid=QS&keyword_orig=sector+45+gurgaon&frm_srp=1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-GB,en-US;q=0.8,en;q=0.6",
        'cookie': "__utmt=1; _ss_v=bWWGBjd7qHlo6HiT; __sonar=4826867768112536344; 99NRI=1; src_city=0; 99_citypage=0; kwp_last_action_id_type=0%2CCP_C%2C130402823599036101; newRequirementsByUser=0; 99_city=1; spd=%7B%22P%22%3A%7B%22a%22%3A%22C%22%2C%22b%22%3A%22S%22%2C%22c%22%3A%22C%22%2C%22d%22%3A%228%22%7D%7D; lsp=P; 99zedoParameters=%7B%22city%22%3A%228%22%2C%22locality%22%3A%222459%2C2470%22%2C%22budgetBucket%22%3Anull%2C%22activity%22%3A%22SRP%22%2C%22rescom%22%3A%22COM%22%2C%22preference%22%3A%22BUY%22%2C%22nri%22%3Anull%7D; _ss_s=eyJsb2NhdGlvbiI6Ikd1cmdhb24gLSBIYXJ5YW5hLCBJbmRpYSIsIklQIjoiMTgyLjc1LjE3My4xNzMiLCJicm93c2VyIjoiQ2hyb21pdW0gNTUuMC4yODgzIiwiT1MiOiJVYnVudHUiLCJyZWZlcnJlciI6IkRpcmVjdCIsInJlcGVhdCI6IlllcyJ9; __utma=267917265.150660647.1484028240.1484718276.1484726617.6; __utmb=267917265.6.7.1484726817579; __utmc=267917265; __utmz=267917265.1484637079.4.4.utmcsr=google|utmgclid=COiIj43QyNECFROVaAodwaQDcg|utmgclsrc=aw.ds|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); ms_cm=%5B%22lv%22%2C%22re%22%2C%22c%22%2C%22pan%22%5D; 99_trackIP=IN; 99_defsrch=m; 99_FP_VISITOR_OFFSET=42; 99_suggestor=19; NEW_VISITOR=1; PROP_SOURCE=IP; sl_user=0; 99_ab=37; RES_COM=RES; GOOGLE_SEARCH_ID=460472684909487403; _sess_id=RO9ogXCOQKLZ2YQH168CQdsGtDvDkRsjSl6DBSIbEZWmOtOBoRtyaje2a6HC5DY2%2F1eSUh%2F49D8g4m6ncSxpPA%3D%3D; __utid=9; _ss_v=bWWGBjd7qHlo6HiT; __sonar=4826867768112536344; 99NRI=1; src_city=0; 99_citypage=0; 99_trackIP=IN; 99_FP_VISITOR_OFFSET=23; 99_suggestor=84; NEW_VISITOR=1; PROP_SOURCE=IP; sl_user=0; 99_ab=27; 99zedoParameters=%7B%22city%22%3A%228%22%2C%22locality%22%3A%222459%22%2C%22budgetBucket%22%3A%22LOW%22%2C%22activity%22%3A%22DET_VIEW%22%2C%22rescom%22%3A%22COM%22%2C%22preference%22%3A%22RENT%22%2C%22nri%22%3Anull%7D; __atuvc=2%7C3; kwp_last_action_id_type=4732079650952892%2CVSP%2C460472684909487403; 99_defsrch=m; 99_city=1; spd=%7B%22P%22%3A%7B%22a%22%3A%22C%22%2C%22b%22%3A%22L%22%2C%22c%22%3A%22C%22%2C%22d%22%3A%228%22%7D%7D; lsp=P; _ss_s=eyJsb2NhdGlvbiI6Ikd1cmdhb24gLSBIYXJ5YW5hLCBJbmRpYSIsIklQIjoiMTgyLjc1LjE3My4xNzMiLCJicm93c2VyIjoiQ2hyb21pdW0gNTUuMC4yODgzIiwiT1MiOiJVYnVudHUiLCJyZWZlcnJlciI6Ind3dy45OWFjcmVzLmNvbS9yZW50LWNvbW1lcmNpYWwtcHJvcGVydHktaW4tc2VjdG9yLTQ1LWd1cmdhb24tZmZpZD9vcmlnX3Byb3BlcnR5X3R5cGU9QyZzZWFyY2hfdHlwZT1RUyZzZWFyY2hfbG9jYXRpb249U0gmcGFnZWlkPVFTIiwicmVwZWF0IjoiWWVzIn0=; newRequirementsByUser=0; _sess_id=5Nt5M1yrtSOUdzrdC1GvbG%2BVohEiABlxX51Us3ZoaQV1DwcNzFy%2BwtSFTK9ibOis7PpGEGpjZC0RUQuyhJqCCQ%3D%3D; __utid=6; __utma=267917265.150660647.1484028240.1484726617.1484728147.7; __utmb=267917265.21.7.1484733366609; __utmc=267917265; __utmz=267917265.1484637079.4.4.utmcsr=google|utmgclid=COiIj43QyNECFROVaAodwaQDcg|utmgclsrc=aw.ds|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); ms_cm=%5B%22lv%22%2C%22re%22%2C%22c%22%2C%22pan%22%5D; GOOGLE_SEARCH_ID=460472684909487403; RES_COM=COM",
        'cache-control': "no-cache",
        'postman-token': "3216de47-f0ed-24c4-1d49-8a40ead1de3f"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    mydict={}
    mydict=response.json()
    for i in range(len(mydict['results'])):
        data=mydict['results'][i]
        with open('Gurgaon.csv', 'a') as f:
          writer = csv.writer(f)
          writer.writerow([' ',data['LOCALITY'],Polygon,lat,lng,data['AREA'],data['AREA_TYPE'],data['AREA_UNIT'],data['PRICE_DISP']])
  except:
     with open('some.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([' ','','','','','','','',''])

    