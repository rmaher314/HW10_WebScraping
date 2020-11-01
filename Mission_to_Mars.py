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
    
def scrape():
    browser = init_browser()
#JLP - Mars Space Images - Featured Image
    mars_data = {}
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    feature.visit(url)

    time.sleep(1)

    full_image_elem = feature.find_by_id('full_image')
    full_image_elem.click()

    html = feature.html
    soup = BeautifulSoup(html, "html.parser")

    img_url_rel = soup.select_one('figure.lede a img').get("src")
    mars_data["src"] = img_url_rel

#NASA Mars News

#Collecting the mars news form nasa.gov.

    url2 = 'https://mars.nasa.gov/news/'
    browser.visit(url2)
    
    time.sleep(1)

    html = feature.html
    soup = BeautifulSoup(html, "html.parser")
    headlines = soup.select_one('ul.item_list li.slide')

    headlines.find("div", class_='content_title')

    news_title = headlines.find("div", class_='content_title').get_text()


    article_teaser = headlines.find("div", class_='article_teaser_body').get_text()
    article_teaser
    mars_data["article_teaser_body"] = article_teaser


#Mars Hemispheres
    url3 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&kl-targets&v1=mars'
    feature.visit(url3)
    time.sleep(2)
    
    html = feature.html
    soup = BeautifulSoup(html, "html.parser")
    
    links_found = feature.links.find_by_partial_href('/search/map/Mars/Viking/')
    
    
    hemispheres = soup.find_all('h3')
    baseUrl = 'https://astrogeology.usgs.gov'
    hemisphere_text = ''
    
    
    for hemisphere in hemispheres:
        #print(hemisphere.text)
        hemisphere_text += hemisphere.text
    #print(hemisphere_text)
    mars_data["hemisphere_text"] = " " + hemisphere_text
    
    counter = 0
    
    imgUrl = ''

    for a in soup.find_all('a', {'class':'itemLink'}):
        counter = counter + 1
        hemisphereurl = baseUrl + a['href']
        if counter % 2 == 0:
            #print (hemisphereurl)
            #imgUrl += " " + hemisphereurl
            feature.visit(hemisphereurl)
            time.sleep(2)
        
            html = feature.html
            soup2 = BeautifulSoup(html, "html.parser")
            full_image_elem = feature.find_by_id('wide-image-toggle')
            full_image_elem.click()
            divs = feature.find_by_tag("img")#[class='wide-image']
            matches = soup2.findAll("img", {"class":"wide-image"})
            
            for match in matches:
                imgUrl += baseUrl + match['src'] + " "
                #print(imgUrl)
            feature.back()
            time.sleep(2)
            
            
    mars_data["imgUrl"] = imgUrl
    #mars_data["hemisphere.text", "hemisphereurl"] = article_teaser

    html = feature.html
    soup = BeautifulSoup(html, "html.parser")
    browser.quit()
    return mars_data