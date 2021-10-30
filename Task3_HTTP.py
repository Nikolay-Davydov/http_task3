import requests
import time

current_date = int(time.time())
cd = str(current_date)
sec = 86400 * 2
cd2 = str(current_date - sec)
tag = 'Python'
url ='https://api.stackexchange.com/2.3/'
responce = requests.get(url + 'search?fromdate=' + cd2 + '&todate='+ cd + '&order=desc&sort=activity&intitle=' + tag + '&site=stackoverflow')
quest_dist = responce.json()
for quest in quest_dist['items']:
    print(quest['title'], '\n') 
