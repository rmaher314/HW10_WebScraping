from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


#Mars Facts Table
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
type(tables)
tables[1]

mars_df = tables[0]
mars_df.columns = ['Data','Mars Facts']
mars_df

mars_df.set_index('Data', inplace=True)
mars_df

html_table = mars_df.to_html()
html_table

mars_df.to_html('mars_table.html')

#Web Scraping
def init_browser():
    executable_path = {"executable_path": "../chromedriver"}
    return 
    feature = Browser("chrome", **executable_path, headless=False)
    

#JLP - Mars Space Images - Featured Image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
feature.visit(url)

time.sleep(1)

full_image_elem = feature.find_by_id('full_image')
full_image_elem.click()

html = feature.html
soup = BeautifulSoup(html, "html.parser")

img_url_rel = soup.select_one('figure.lede a img').get("src")
img_url_rel

#NASA Mars News

#Collecting the mars news form nasa.gov.
url2 = 'https://mars.nasa.gov/news/'
feature.visit(url2)

time.sleep(1)

html = feature.html
soup = BeautifulSoup(html, "html.parser")
headlines = soup.select_one('ul.item_list li.slide')

headlines.find("div", class_='content_title')

news_title = headlines.find("div", class_='content_title').get_text()
news_title

article_teaser = headlines.find("div", class_='article_teaser_body').get_text()
article_teaser

#Mars Hemispheres