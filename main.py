#step 1 install bs4, install requests ,install pandas3
import pandas as pd
import requests
from bs4 import BeautifulSoup
url = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324')
soup= BeautifulSoup(url.content,'html.parser')
#print(soup)
#print(soup.find_all('a'))
week= soup.find(id='seven-day-forecast-body')
#print(week) #shows everything inside div id
items =week.find_all(class_ = 'tombstone-container')
#print(items)
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
period_names = [ item.find(class_ ='period-name').get_text() for item in items ]
print (period_names)
short_descriptions = [ item.find(class_ ='short-desc').get_text() for item in items ]
print(short_descriptions)
temperatures= [ item.find(class_ ='temp').get_text() for item in items ]
print(temperatures)
whether_stuff = pd.DataFrame(
    {'period-name': period_names,
    'short-desc':short_descriptions,
    'temp':temperatures}
)
print(whether_stuff)
whether_stuff.to_csv('beautiful_soup.csv')