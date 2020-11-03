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
    executable_path = {"executable_path": "./chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
    
def scrape():
    print("scraping mars")
    feature = init_browser()
#JLP - Mars Space Images - Featured Image
    mars_data = {}
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    feature.visit(url)

    time.sleep(1)

    full_image_button = feature.find_by_id("full_image")
    full_image_button.click()

    # Find "More Info" Button and Click It
    feature.is_element_present_by_text("more info", wait_time=2)
    more_info_element = feature.find_link_by_partial_text("more info")
    more_info_element.click()
# #Added this element in
#     feature.is_element_present_by_text('more info', wait_time=1)
#     more_info_elem = feature.links.find_by_partial_text('more info')
#     more_info_elem.click()
# #Added Element Complete

    html = feature.html
    soup = BeautifulSoup(html, "html.parser")
    try:
       #feature_img = soup.select_one("figure.lede a img").get("src")
       feature_img = soup.find("img", class_="main_image")
    except AttributeError:
       return None
   # Use Base URL to Create Absolute URL
    feature_img = f"https://www.jpl.nasa.gov{feature_img['src']}"
    
    mars_data["feature_img"] = feature_img
#NASA Mars News

#Collecting the mars news form nasa.gov.
    print("visiting 2nd url")
    url2 = 'https://mars.nasa.gov/news/'
    feature.visit(url2)
    
    time.sleep(1)

    html = feature.html
    soup = BeautifulSoup(html, "html.parser")
    headlines = soup.select_one('ul.item_list li.slide')

    headlines.find("div", class_='content_title')

    news_title = headlines.find("div", class_='content_title').get_text()
    mars_data["news_title"] = news_title

    article_teaser = headlines.find("div", class_='article_teaser_body').get_text()
    article_teaser
    mars_data["article_teaser_body"] = article_teaser


#Mars Hemispheres
    print("visiting 3rd url")
    url3 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&kl-targets&v1=mars'
    feature.visit(url3)
    time.sleep(2)
    
    html = feature.html
    soup = BeautifulSoup(html, "html.parser")
    
    links_found = feature.links.find_by_partial_href('/search/map/Mars/Viking/')
    
    
    hemispheres = soup.find_all('h3')
    baseUrl = 'https://astrogeology.usgs.gov'
    
    hemisphere_info = []
    #imageUrl = ''
    counter = 0
    keyCounter = 0;    

    for a in soup.find_all('a', {'class':'itemLink'}):
        counter = counter + 1
        hemisphereurl = baseUrl + a['href']
        if counter % 2 == 0:
            

            feature.visit(hemisphereurl)
            time.sleep(2)
            
            html = feature.html
            soup2 = BeautifulSoup(html, "html.parser")
            
            hemi_info = {}


            hemisphere_name = soup2.find("h2", {"class":"title"}).text

            hemi_info["title"] = hemisphere_name



            divs = feature.find_by_tag("img")#[class='wide-image']
            matches = soup2.find("img", {"class":"wide-image"}).get("src")
            
            hemi_url = baseUrl + matches
            hemi_info["url"] = hemi_url

            hemisphere_info.append(hemi_info)

            # print(hemisphere_name)
            # print(imageUrl)
            # name = "name"+ str(keyCounter)
            # link = "link"+str(keyCounter)
            # keyCounter = keyCounter +1
            # if len(hemisphere_info)==0:
            #    hemisphere_info ={
            #     name: hemisphere_name,
            #     link: imageUrl
            # }
            # else:
            #     hemisphere_info.update({
            #         name: hemisphere_name,
            #         link: imageUrl
            #     })
            # print(hemisphere_info)   
            feature.back()
            time.sleep(2)
                
    print("exited loop")           
    mars_data["hemisphere_info"] = hemisphere_info
    # html = feature.html
    # soup = BeautifulSoup(html, "html.parser")
    feature.quit()
    return mars_data