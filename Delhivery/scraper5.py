import requests
import csv
with open('HS_Gurgaon.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['City','District','Housing-Region','Locality','Sub-Locality','Polygon','Center_Cordinates','building_name','area','formatted_max_price','formatted_min_price','formatted_per_sqft_rate'])

with open('HS_Gurgaon.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['Gurgaon','','','','','','','','','','','',''])

uuids=['cdbadacafda35b98d359']
completed=[]
while not not(uuids):
    ids=uuids.pop()
    if ids not in completed:
        
        print("Getting details for city uuid %s" % ids)
        try:
            url = "https://regions.housing.com//api/v2/polygon/client/show/bulk"

            querystring = {"source":"web","uuids":ids,"keys":"uuid,polygon,name,feature_type,center"}

            headers = {
                'accept': "application/json, text/plain, */*",
                'app_name': "desktop_web",
                'origin': "https://housing.com",
                'x-devtools-emulate-network-conditions-client-id': "930b8cdd-7f50-4c08-a7f6-daf46e92e68b",
                'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36",
                'referer': "https://housing.com/in/buy/search?f=eyJzaG93RmlsdGVyU3VnZ2VzdGlvbiI6ZmFsc2UsInYiOjIsInMiOiJkIiwidXNlckNpdHkiOiIxMWUxMjA4MWFhNzhhMzM3NTA4NyIsImJhc2UiOlt7InR5cGUiOiJQT0xZIiwidXVpZCI6ImQxMmY5MDc0NGM2YzQ0M2UyYTFlIiwibGFiZWwiOiJTZWN0b3IgNDYifV0sInN1Z2dlc3Rpb25Db3VudCI6MzIwNjZ9",
                'accept-encoding': "gzip, deflate, sdch, br",
                'accept-language': "en-GB,en-US;q=0.8,en;q=0.6",
                'cache-control': "no-cache",
                'postman-token': "7046eeb2-ba83-0ae3-2c07-caf7aebfaaec"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)

            d={}
            d=response.json()

            Center_Cordinates=(d[0]['center'])
            Sector=(d[0]['name'])
            
            Polygon=(d[0]['polygon']['coordinates'][0])

            url = "https://buy.housing.com//api/v3/buy/index/filter"

            querystring = {"source":"web","poly":ids,"sort_key":"relevance","tag_suggestions":"true","p":"3","total":"940","np_total_count":"14","resale_total_count":"926","np_offset":"0","resale_offset":"0","is_last_page":"false","project_flat_config_count":"14","negative_aggregation":"%7B%7D","seedsShown":"true","results_per_page":"10","show_collections":"true","show_aggregations":"true","placeholder_ids":"2,3,6,7"}

            headers = {
            'accept': "application/json, text/plain, */*",
            'x-csrf-token-v2': "40dbb1cc800f65a263329c56483ca2037190ef345ce644ce67f3173d3a6c0e5e",
            'app_name': "desktop_web",
            'origin': "https://housing.com",
            'x-devtools-emulate-network-conditions-client-id': "930b8cdd-7f50-4c08-a7f6-daf46e92e68b",
            'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36",
            'referer': "https://housing.com/in/buy/search?f=eyJzaG93RmlsdGVyU3VnZ2VzdGlvbiI6ZmFsc2UsInYiOjIsInMiOiJkIiwidXNlckNpdHkiOiIxMWUxMjA4MWFhNzhhMzM3NTA4NyIsImJhc2UiOlt7InR5cGUiOiJQT0xZIiwidXVpZCI6ImQxMmY5MDc0NGM2YzQ0M2UyYTFlIiwibGFiZWwiOiJTZWN0b3IgNDYifV0sInN1Z2dlc3Rpb25Db3VudCI6MzIwNjZ9",
            'accept-encoding': "gzip, deflate, sdch, br",
            'accept-language': "en-GB,en-US;q=0.8,en;q=0.6",
            'cookie': "traffic=sourcemedium%3Ddirect%20%2F%20none%3B; uuid=id%3Db84eac5941a4bab0e141668e273cda9c%3B; last_selected_city=35; last_selected_city_uuid=526acdc6c33455e9e4e9; _gat=1; _udata_=time%3D1484820019615%3B; cuid=ff4da29b-d74d-45b0-b962-14176ba58437; experiments=show_video_ad%3Dtrue%3Bshow_recommended%3Dfalse%3Bshow_map%3Dfalse%3B; _ga=GA1.2.733690436.1484029481; _housing_np-buy_session=U1l1RFNRazlTemIyZ2h0R3RBRzJNZjBUSmo0RXM2alY0S2wzeUQrRFZUVldQS2h1WmtuZW02RjZDVTdFQzBoVzVyS0tvV1VBV01ZSmZZNlh5dTBkVWtLYUw1OG5FUkhkSFU2YURWTVpWbTdyRm4wcnA1cmQvd3p6NFArbjlCOUwtLVJxekV5d1d1TnpMSzRRRzdQejY4Ymc9PQ%3D%3D--c5ca565b494d34c39f5db9d14e5160763009723a",
            'cache-control': "no-cache",
            'postman-token': "6b5c3b3b-a673-404c-b055-911f013006ae"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            mydict={}
            mydict=response.json()
            
            for j in range(len(mydict['hits'])):
                
                building_name=mydict['hits'][j]['building_name']
                formatted_max_price=mydict['hits'][j]['formatted_max_price']
                formatted_min_price=mydict['hits'][j]['formatted_min_price']
                formatted_per_sqft_rate=mydict['hits'][j]['formatted_per_sqft_rate']
                formatted_price=mydict['hits'][j]['formatted_price']
                area=mydict['hits'][j]['inventory_configs'][0]['area']


                city=mydict['hits'][j]['polygons_hash']['city']['name']
                District=mydict['hits'][j]['polygons_hash']['h_district']['name']
                Housing_Region=mydict['hits'][j]['polygons_hash']['h_district']['name']
                Locality=mydict['hits'][j]['polygons_hash']['locality']['name']
                Sub_Locality=mydict['hits'][j]['polygons_hash']['sublocality']['name']


                with open('HS_Gurgaon.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(['',District,Housing_Region,Locality,Sub_Locality,Polygon,Center_Cordinates,building_name,area,formatted_max_price,formatted_min_price,formatted_per_sqft_rate])
                polList=mydict['hits'][j]['polygon_uuids']
                for i in range(len(polList)):
                    if polList[i] not in uuids:
                        uuids.append(polList[i])
            completed.append(ids)
        except:
            with open('HS_Gurgaon.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(['','','','','','','','','','','',''])

