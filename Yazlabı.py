# importing the library
import requests
from bs4 import BeautifulSoup
# enter city name
city = "istanbul"

# create url
url = "https://www.google.com/search?q="+"weather"+city

# requests instance
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# format the data
data = str.split('\n')
time = data[0]
sky = data[1]
# list having all div tags having particular class name
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# particular list with required data
strd = listdiv[5].text

# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]
# printing all the data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# Enter city name
city = "İstanbul"

# Creating URL and making requests instance
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content

# Getting raw data using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extracting the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# Extracting the time and sky description
str_ = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str_.split('\n')
time = data[0]
sky = data[1]

# Getting all div tags with the specific class name
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# Extracting other required data
strd = listdiv[5].text
pos = strd.find('Wind')
other_data = strd[pos:]

# Printing the extracted weather data
print("Temperature is:", temp)
print("Time:", time)
print("Sky Description:", sky)
print(other_data)
