from bs4 import BeautifulSoup
import requests
import pandas as pd

course_title=[]
author_name=[] 
ratings=[]
prices=[]

url = 'https://www.udemy.com/topic/python/'
response = requests.get(url)
cont = response.content

soup = BeautifulSoup(cont,"html.parser")

for a in soup.find_all('div', attrs={'class':'course-card--main-content--2XqiY course-card--has-price-text--1c0ze'}): 
      
    name=a.find('div', attrs={'class':'udlite-focus-visible-target udlite-heading-md course-card--course-title--vVEjC'})
    author=a.find('div', attrs={'class':'udlite-text-xs course-card--instructor-list--nH1OC'})
    rating=a.find('span', attrs={'class':'udlite-heading-sm star-rating--rating-number--2o8YM'})
    price=a.find('div', attrs={'class':'price-text--price-part--2npPm course-card--discount-price--1bQ5Q udlite-heading-md'})
    course_title.append(name.text)
    author_name.append(author.text)
    ratings.append(rating.text)
    prices.append(price.text)


df = pd.DataFrame({'Course Title':course_title,'Author':author_name,'Price':prices,'Rating':ratings}) 
df.to_csv('courses.csv', index=False, encoding='utf-8')
