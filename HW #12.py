#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests


# In[2]:


executable_path = {'executable_path': r"C:\Users\jimkn\Downloads\chromedriver (4).exe"}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = ('https://mars.nasa.gov/news/')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:


print(soup.prettify())


# NASA Mars News

# In[ ]:


# pull titles
titles = soup.find_all('div', class_="content_title")
print(titles)


# In[ ]:


# pull body from website
body = soup.find_all('div', class_="rollover_description")
print(body)


# In[ ]:


#titles
broadcast_title = "NASA to Broadcast Mars 2020 Perseverance Launch, Prelaunch Activities"
broadcast_p = "Starting July 27, news activities will cover everything from mission engineering and science to returning samples from Mars to, of course, the launch itself"
launch_title = "The Launch Is Approaching for NASA's Next Mars Rover, Perseverance"
launch_p = "The Red Planet's surface has been visited by eight NASA spacecraft. The ninth will be the first that includes a roundtrip ticket in its flight plan."
rover_title = "NASA to Hold Mars 2020 Perseverance Rover Launch Briefing"
rover_p = "Learn more about the agency's next Red Planet mission during a live event on June 17."
student_title = "Alabama High School Student Names NASA's Mars Helicopter"
student_p = "Vaneeza Rupani's essay was chosen as the name for the small spacecraft, which will mark NASA's first attempt at powered flight on another planet."
helicopter_title = "Mars Helicopter Attached to NASA's Perseverance Rover"
helicopter_p = "The team also fueled the rover's sky crane to get ready for this summer's history-making launch."
wheels_title = "NASA's Perseverance Mars Rover Gets Its Wheels and Air Brakes"
wheels_p = "After the rover was shipped from JPL to Kennedy Space Center, the team is getting closer to finalizing the spacecraft for launch later this summer."


# In[ ]:



# pull titles and body from website
results = soup.find_all('div', class_="slide")
for result in results:
    titles = result.find('div', class_="content_title")
    title = titles.find('a').text
    bodies = result.find('div', class_="rollover_description")
    body = bodies.find('div', class_="rollover_description_inner").text
    print('----------------')
    print(title)
    print(body)


# JPL Mars Space Images - Featured Image

# In[ ]:


url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:


print(soup.prettify())


# In[ ]:


# pull images from website
images = soup.find_all('a', class_="fancybox")
print(images)


# In[ ]:


# pull image link
pic_src = []
for image in images:
    pic = image['data-fancybox-href']
    pic_src.append(pic)


# In[ ]:


featured_image_url = 'https://www.jpl.nasa.gov' + pic
featured_image_url


# Mars Weather

# In[ ]:



url = ('https://twitter.com/marswxreport?lang=en')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:



weather_soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:


#grab all the tweets in case the first one isn't the one you want
mars_weather_tweet = weather_soup.find_all('div', class_ = "js-tweet-text-container")


# In[3]:


weather_mars = []
for content in contents:
    tweet = content.find("div", class_="js-tweet-text-container").text
    weather_mars.append(tweet)
print(weather_mars)


# In[4]:


for tweet in mars_weather_tweet:
    if tweet.text.strip().startswith('Sol'):
        mars_weather = tweet.text.strip()
        


# Mars Facts

# In[5]:


mars_facts_url = "https://space-facts.com/mars/"
table = pd.read_html(mars_facts_url)
table[0]


# In[6]:


df = table[0]
df.columns = ["Facts", "Value"]
df.set_index(["Facts"])
df


# In[7]:


facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# Mars Hemispheres

# In[11]:


url = ('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
browser.visit(url)


# In[9]:


print(soup.prettify())


# In[13]:


import time 
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
mars_hemis=[]


# In[14]:


# loop through the four tags and load the data to the dictionary

for i in range (4):
    time.sleep(5)
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    dictionary={"title":img_title,"img_url":img_url}
    mars_hemis.append(dictionary)
    browser.back()


# In[15]:


print(mars_hemis)


# In[ ]:




