
# Dependencies
import os
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests

# Dictionary to store scraped data
mars_data = {}

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()


    # Create a new Browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit the site
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    # Create a Beautiful Soup object - use bs to write it into HTML
    html = browser.html
    news_soup = bs(html, 'html.parser')

    # Extract most current title text
    news_title = news_soup.find('div', class_="content_title").text
    mars_data['news_title'] = news_title
    # print(news_title)

    # Extract most current paragraph text 
    news_paragraph = news_soup.find('div', class_="article_teaser_body")
    mars_data['news_paragraph'] = news_paragraph
    # print(news_paragraph)

    # Print the variables for the title and paragraph text 
    #print(f"The most current news title is {news_title}.")
    #print(f"The paragraph says {news_paragraph}.")


    # ### JPL Mars Space Images - Featured Image

    # Create a new Browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Navigate to the page
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    # Get the tile of the page
    browser.title

    # Get the full image
    browser.click_link_by_partial_text('FULL IMAGE')

    jpl_html = browser.html
    jpl_soup = bs(html, 'html.parser')

    img_find = jpl_soup.find('img', class_='fancybox-image')
    featured_image_url = f'https://www.jpl.nasa.gov{img_find}'

    mars_data['featured_image_url'] = featured_image_url
    #print(featured_image_url)




    # ### Mars Weather

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    twitter_html = browser.html
    soup = bs(twitter_html, "html.parser")

    # Save the tweet text as mars_weather
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_data['mars_weather'] = mars_weather
    # print(mars_weather)



    # ### Mars Facts

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)


    facts_html = browser.html
    soup = bs(facts_html, "html.parser")

    facts_scrape_df = pd.read_html(facts_url)
    facts_scrape_df[0]

    # Change column names 
    facts_scrape_df[0].columns = ['Mars Trait', 'Information']

    facts_scrape_df[0]

    # Use Pandas to convert the data to a HTML table string
    facts_html = facts_scrape_df[0].to_html()
    # facts_html
    mars_data['facts_html'] = facts_html


    # ### Mars Hemispheres

    # Dictionary to store titles and URLs
    hemisphere_img_urls = []


    # #### Cerberus Hemisphere

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)

    cerberus_html = browser.html
    soup = bs(cerberus_html, "html.parser")

    cerberus_image = soup.find_all('div', class_="wide-image-wrapper")
    # print(cerberus_image)
    mars_data['cerberus_image'] = cerberus_image

    # find image url
    for image in cerberus_image:
        img = image.find('li')
        ce_full_img_url = img.find('a')['href']
        # print(ce_full_img_url)
        mars_data['ce_full_img_url'] = ce_full_img_url

    # find image title
    cerberus_title = soup.find('h2', class_='title').text
    # print(cerberus_title)
    mars_data['cerberus_title'] = cerberus_title


    # append to dictionary
    hemisphere_img_urls.append({"title": cerberus_title, "img_url": ce_full_img_url})


    # #### Schiaparelli Hemisphere

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    schia_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(schia_url)

    schia_html = browser.html
    soup = bs(schia_html, "html.parser")

    schia_image = soup.find_all('div', class_="wide-image-wrapper")
    # print(schia_image)
    mars_data['schia_image'] = schia_image


    # find image url
    for image in schia_image:
        img = image.find('li')
        sc_full_img_url = img.find('a')['href']
        # print(sc_full_img_url)
        mars_data['sc_full_img_url'] = sc_full_img_url



    # find image title
    schia_title = soup.find('h2', class_='title').text
    # print(schia_title)
    mars_data['schia_title'] = schia_title

    hemisphere_img_urls.append({"title": schia_title, "img_url": sc_full_img_url})


    ##### Syrtis Major Hemisphere

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtis_url)

    syrtis_html = browser.html
    soup = bs(syrtis_html, "html.parser")

    syrtis_image = soup.find_all('div', class_="wide-image-wrapper")
    # print(syrtis_image)
    mars_data['syrtis_image'] = syrtis_image


    # find image url
    for image in syrtis_image:
        img = image.find('li')
        sy_full_img_url = img.find('a')['href']
        # print(sy_full_img_url)
        mars_data['sy_full_img_url'] = sy_full_img_url


    # find image title
    syrtis_title = soup.find('h2', class_='title').text
    # print(syrtis_title)
    mars_data['syrtis_title'] = syrtis_title


    hemisphere_img_urls.append({"title": syrtis_title, "img_url": sy_full_img_url})


    ##### Valles Marineris Hemisphere

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    valles_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(valles_url)

    valles_html = browser.html
    soup = bs(valles_html, "html.parser")


    valles_image = soup.find_all('div', class_="wide-image-wrapper")
    # print(valles_image)
    mars_data['valles_image'] = valles_image


    # find image url
    for image in valles_image:
        img = image.find('li')
        va_full_img_url = img.find('a')['href']
        # print(va_full_img_url)
        mars_data['va_full_img_url'] = va_full_img_url


    # find image title
    valles_title = soup.find('h2', class_='title').text
    # print(valles_title)
    mars_data['valles_title'] = valles_title


    hemisphere_img_urls.append({"title": valles_title, "img_url": va_full_img_url})

    # Print dictionary 
    # print(hemisphere_img_urls)
    mars_data['hemisphere_img_urls'] = hemisphere_img_urls

    print(mars_data)

scrape()