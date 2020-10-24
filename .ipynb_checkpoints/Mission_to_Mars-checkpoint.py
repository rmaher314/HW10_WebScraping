{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "\n",
    "def init_browser():\n",
    "    # @NOTE: Replace the path with your actual path to the chromedriver\n",
    "    executable_path = {\"executable_path\": \"chromedriver\"}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)\n",
    "\n",
    "\n",
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    # create surf_data dict that we can insert into mongo\n",
    "    mars_news = {}\n",
    "\n",
    "    # visit unsplash.com\n",
    "    url = \"https://mars.nasa.gov/news/\"\n",
    "    browser.visit(url)\n",
    "\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, \"html.parser\")\n",
    "\n",
    "    mars_news[\"news_title\"] = soup.find(\"div\", class_=\"content_title\").get_text()\n",
    "    mars_news[\"news_p\"] = soup.find(\"a\", class_=\"href\").get_text()\n",
    "\n",
    "    return mars_news"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
