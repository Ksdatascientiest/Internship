#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1) Write a python program to display all the header tags from wikipedia.org and make data frame.

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# In[6]:


#  2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) from https://presidentofindia.nic.in/former-presidents.htm and make data frame

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://presidentofindia.nic.in/former-presidents"
response = requests.get(url)
 # print(response)

soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")
names = []
terms = []
for row in table.find_all("tr")[1:]:
    columns = row.find_all("td")
    name = columns[0].text.strip()
    term = columns[1].text.strip()
    names.append(name)
    terms.append(term)
    data = {"Name": names, "Term of Office": terms}
    df = pd.DataFrame(data)
    print(df)


# In[2]:


#  3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame

#  a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

batsman_data = []
table = soup.find("table", class_="table")
rows = table.find_all("tr")

for row in rows[1:11]:
    cells = row.find_all("td")
    batsman = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    batsman_data.append([batsman, team, rating])

df = pd.DataFrame(batsman_data, columns=["Batsman", "Team", "Rating"])
print(df)


# In[7]:


#b) Top 10 ODI Batsmen along with the records of their team andrating.
#c) Top 10 ODI bowlers along with the records of their team andrating


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.content, "lxml")

bowler_data = []
table = soup.find("table", class_="table")
rows = table.find_all('tr')

for row in rows[1:11]:
 cells = row.find_all('td')
 bowler = cells[1].text.strip()
 team = cells[2].text.strip()
 rating = cells[3].text.strip()
 bowler_data.append([bowler, team, rating])

df = pd.DataFrame(bowler_data, columns=["Bowler", "Team", "Rating"])
print(df)


# In[ ]:


#4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
     # a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
    # b) Top 10 women’s ODI Batting players along with the records of their team and rating.
   # c) Top 10 women’s ODI all-rounder along with the records of their team and rating.


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scrape Top 10 ODI teams in women's cricket
url_teams = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
response_teams = requests.get(url_teams)
#print(response)

soup_teams = BeautifulSoup(response_teams.content, "lxml")
print(soup)

teams_data = []
table_teams = soup_teams.find("table", class_="table")
rows_teams = table_teams.find_all("tr")

for row in rows_teams[1:11]:
    team_name = row.find("span", class_="u-hide-phablet").text.strip()
    matches = row.find_all("td")[2].text.strip()
    points = row.find_all("td")[3].text.strip()
    rating = row.find_all("td")[4].text.strip()
    teams_data.append([team_name, matches, points, rating])
    
# Scrape Top 10 women's ODI Batting players
url_batting = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
response_batting = requests.get(url_batting)
soup_batting = BeautifulSoup(response_batting.content, "lxml")
print(soup_batting)
batting_data = []
table_batting = soup_batting.find("table", class_="table")
rows_batting = table_batting.find_all("tr")
for row in rows_batting[1:11]:
    player_name = row.find("td", class_="table-body__cell rankings-table__name name").text.strip()
    team = row.find("span", class_="table-body__logo-text").text.strip()
    rating = row.find("td", class_="table-body__cell rating").text.strip()
    batting_data.append([player_name, team, rating])

# Scrape Top 10 women's ODI all-rounders
url_allrounders = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"
response_allrounders = requests.get(url_allrounders)
soup_allrounders = BeautifulSoup(response_allrounders.content, "html.parser")

allrounders_data = []
table_allrounders = soup_allrounders.find("table", class_="table")
rows_allrounders = table_allrounders.find_all("tr")

for row in rows_allrounders[1:11]:
  player_name = row.find("td", class_="table-body__cell rankings-table__name name").text.strip()
  team = row.find("span", class_="table-body__logo-text").text.strip()
  rating = row.find("td", class_="table-body__cell rating").text.strip()
  allrounders_data.append([player_name, team, rating])

# Create data frames
df_teams = pd.DataFrame(teams_data, columns=["Team", "Matches", "Points", "Rating"])
df_batting = pd.DataFrame(batting_data, columns=["Player", "Team", "Rating"])
df_allrounders = pd.DataFrame(allrounders_data, columns=["Player", "Team", "Rating"])

# Print the data frames
print("Top 10 ODI teams in women's cricket:")
print(df_teams)
print("\nTop 10 women's ODI Batting players:")
print(df_batting)
print("\nTop 10 women's ODI all-rounders:")
print(df_allrounders)


# In[42]:


# 5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame
  #    i) Headline
  #   ii) Time
  #  iii) News Link

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)

#print (response)
soup = BeautifulSoup(response.text,"lxml")
print(soup)

# Find all the news articles on the page
articles = soup.find_all("div", class_="Card-titleContainer")

# Initialize empty lists to store the scraped data
headlines = []
times = []
links = []

for article in articles:
    
    headline = article.find("a").text.strip()
    headlines.append(headline)
    
    time = articles.find("time").text.strip()
    times.append(time)
    
    
  
    link = article.find("a")["href"]
    links.append(link)

# Create a dataframe using the scraped data
data = {
  "Headline": headlines,
  "Time": times,
  "News Link": links
}
df = pd.DataFrame(data)

# Print the dataframe
print(df)


# In[8]:


#6) Write a python program to scrape the details of most downloaded articles from AI in last 90days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articlesScrape below mentioned details and make data frame
#i) Paper Title
#ii) Authors
#iii) Published Date
#iv) Paper URL

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the URL
url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)

articles_container = soup.find("div", class_="pod-listing")
titles = []
authors = []
dates = []
urls = []
for article in articles_container.find_all("li"):
    title = article.find("h3").text.strip()
    titles.append(title)
    author = article.find("span", class_="text-xs").text.strip()
    authors.append(author)
    date = article.find("span", class_="text-xs").find_next_sibling("span").text.strip()
    dates.append(date)
    url = article.find("a")["href"]
    urls.append(url)
    data = {"Paper Title": titles,"Authors": authors,"Published Date": dates,"Paper URL": urls}
    df = pd.DataFrame(data)
    print(df)


# In[12]:


#7) Write a python program to scrape mentioned details from dineout.co.inand make data frame
     #i) Restaurant name
     #ii) Cuisine
     #iii) Location
     #iv) Ratings
     #v) Image UR
    
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.dineout.co.in"
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
restaurant_names = soup.find_all('h2', class_='restnt-name ellipsis')
cuisines = soup.find_all('span', class_='double-line-ellipsis')
locations = soup.find_all('span', class_='double-line-ellipsis')
ratings = soup.find_all('span', class_='rating-value')
image_urls = soup.find_all('img', class_='img-responsive')

# Create empty lists to store the scraped data
restaurant_list = []
cuisine_list = []
location_list = []
rating_list = []
image_url_list = []

for name in restaurant_names:
    restaurant_list.append(name.text.strip())
for cuisine in cuisines:
    cuisine_list.append(cuisine.text.strip())
for location in locations:
    location_list.append(location.text.strip())
for rating in ratings:
    rating_list.append(rating.text.strip())
for image in image_urls:
    image_url_list.append(image['src'])
    data = {Restaurant Name': restaurant_list,'Cuisine': cuisine_list,'Location': location_list,'Ratings': rating_list,'Image URL': image_url_list }
df = pd.DataFrame(data)
print(df)


# In[ ]:




