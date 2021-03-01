# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import requests
import warnings

def init_browser():
    fpath = os.path.normpath(r"C:\Users\felix\OneDrive\Documents\DATA ANALYTICS\HOMEWORK\chromedriver.exe")
    executable_path = {"executable_path": fpath}
    return Browser("chrome", **executable_path, headless=False)

# Create Global Dictionary
mars_data ={}

# NASA Mars News
def scrape_mars_news():

    #Initialize browser
    browser = init_browser()

    #Visit NASA News url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # Scrape site for latest News Title and Paragraph Text
    news_title = browser.find_by_css("div.content_title a").text
    news_p = browser.find_by_css("div.article_teaser_body").text

    # Dictionary entry from Mars News
    mars_data["news_title"] = news_title
    mars_data["news_paragraph"] = news_p

    browser.quit()
    
    return mars_data


# Featured Image
def scrape_featured_image():

    #Initialize browser
    browser = init_browser()

    #Visit Featured Image url
    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(url)

    # Find image url to the fullsize featured image
    featured_image = browser.find_by_css("body > div.header > img")

    # Retrieve url of the full image
    for link in featured_image:
        featured_image_url = (link['src'])
    
        #Dictionary entry for featured image
        mars_data["featured_image_url"] = featured_image_url
    
    browser.quit()
        
    return mars_data


# Mars Facts
def scrape_mars_facts():

    #Initialize browser
    browser = init_browser()

    #Retrieve tables from url
    url = "https://space-facts.com/mars"
    tables = pd.read_html

    #Retrieve and format table wanted
    mars_facts_df = tables[0]
    mars_facts_df.columns = ["Mars", "Value"]
    mars_facts_df.set_index("Mars", inplace=True)

    #Create table html
    mars_html = mars_facts_df.to_html()

    #Dictionary entry for Mars Facts
     mars_data["mars_facts"] = mars_html

     browser.quit()

     return mars_data


# Mars Hemispheres
def scrape_hemispheres():

    #Initialize browser
    browser = init_browser()

    #Retrieve tables from url
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(image_url)

    #Cerberus
    cerberus_image = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(1) > a > img")
    for link in cerberus_image:
        cerberus_url = (link['src'])
    
    #Schiaparelli
    schiaparelli_image = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(2) > a > img")
    for link in schiaparelli_image:
        schiaparelli_url = (link['src'])
    
    #Syrtis Major
    syrtis_image = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(3) > a > img")
    for link in syrtis_image:
        syrtis_url = (link['src'])

    #Valles Marineris
    valles_image = browser.find_by_css("#product-section > div.collapsible.results > div:nth-child(3) > a > img")
    for link in valles_image:
        valles_url = (link['src'])

    
    # Append the dictionary with the image url string and the hemisphere title to a list
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url},
    ]

    #Dictionary entry for Mars Hemispheres
    mars_data["hiu"] = hemisphere_image_urls
    
    browser.quit()

    return mars_data