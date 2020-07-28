# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import time
import re

import pandas as pd
import pprint

def scrape():
    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define database and collection
    db = client.nasa_db
    collection = db.news

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'lxml'
    soup = bs(response.text, 'lxml')

    # Examine the results, then determine element that contains sought info
    results = soup.find_all('div', class_='slide')


    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return title of listing
            title = result.find('div', class_='content_title').text

            # Identify and return the description
            article = result.find('div', class_='rollover_description_inner').text


            # Run only if title, price, and link are available
            if (title and article):
            #if (article):
                # Print results
                # print('-------------')
                # print(title)
                # print(article)


                # Dictionary to be inserted as a MongoDB document
                post = {
                    'title': title,
                    'article': article
                }

                collection.insert_one(post)

        except Exception as e:
            print(e)

        
    # Display items in MongoDB collection
    news_listings = db.news.find()

    for listing in news_listings:
        print(listing)


        #try:
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    #except Exception as e:
    #    print(e)

    #featured_image_url
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Iterate through all pages
    #for x in range(50):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup_mars = bs(html, 'html.parser')


    # Retrieve all elements that contain book information
    articles = soup_mars.find_all('ul', class_='articles')
    print(articles)    


    url_link = []
    image_list = []
    collection1 = db.image_mars

    # Iterate through each book
    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        line = article.find('li')
        link = line.find('a')
        href = link['data-fancybox-href']
    #        title = link['title']
        print('-----------')
        print(href)
        print('https://www.jpl.nasa.gov' + href)
        full_href = ('https://www.jpl.nasa.gov' + href)
        url_link.append(href)
    #    image_list = ['https://www.jpl.nasa.gov' + url for url in url_link]
                    # Dictionary to be inserted as a MongoDB document
        post1 = {
            'href': full_href,
        }
                
        collection1.insert_one(post1)

    # Click the 'Next' button on each page
    try:
        browser.click_link_by_partial_text('next')

    except:
        print("Scraping Complete")


        #featured_image_url
    url_twitter = 'https://twitter.com/marswxreport?lang=en'

    # Iterate through all pages
    for x in range(1):
        # HTML object
        html_twitter = browser.html
        # Parse HTML with Beautiful Soup
        soup_twitter = bs(html_twitter, 'html.parser')
        #print(soup_twitter.prettify())
        # Retrieve all elements that contain book information
        #tweets = soup_twitter.find_all('span')[0]
        tweets = soup_twitter.find_all("span", {"class": re.compile("^css-")})
        #print(tweets)  
        print(tweets)

        x=1
        collection2 = db.weather
        for tweet in tweets:
    #        msg=(tweet.text)
    #            print(msg)
    #        try:
            if((tweet.text.find('InSight')==0) and x==1): 
                
    #           print(tweet.text.is_text_present('InSight'))
    #            print(tweet.is_text_present('InSight'))
                print(tweet.text, type(tweet.text))
    #            print('page:', x, '-------------')
    #            print((tweet.text).startswith('InSight'))
                print(tweet.text)
                weather = tweet.text
                time.sleep(3)
                post2 = {
                    'weather': weather,
                }

                collection2.insert_one(post2)
    #        except tweet.text = '@MarsWxReport':
    #            print('NO')
            #collection.insert_one(post)
    #        browser.quit()
                x+=1
    #    browser.click_link_by_partial_text('Next')
        #except (ElementDoesNotExist):
    
        url_facts = 'https://space-facts.com/mars/'

        type(tables)

    #Comparision information
    df_facts = tables[1]
    #df.columns = ['Equatorial Diameter', 'Polar Diameter', 'Mass', 'Moons', 
    #              'Orbit Distance', 'Orbit Period', 'Surface Temperature', 'First Record', 
    #              'Recorded By']

    df_facts.columns = ['Comparision', 'Mars', 'Earth']

    df_facts.head()


    #Information
    df_factd = tables[0]
    #df_factd.columns = ['Equatorial Diameter', 'Polar Diameter', 'Mass', 'Moons', 
    #              'Orbit Distance', 'Orbit Period', 'Surface Temperature', 'First Record', 
    #              'Recorded By']

    df_factd.columns = ['data_name', 'mars_data']

    df_factd.head(9)

    #make html page
    html_fact_table = df_factd.to_html()
    html_fact_table

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url_mars_img = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_mars_img)

    html = browser.html
    soup_mars_img = bs(html, 'html.parser')

    img_links = soup_mars_img.find_all('div', class_='item')
    img_links

    img_link_news = []

    for img_link in img_links:
        next_url = img_link.find('a')['href']
    #        next_url = link
        print(next_url)
    #    url_list.append(book_url)
        print('https://astrogeology.usgs.gov/' + next_url)
        long_next_url = ('https://astrogeology.usgs.gov' + next_url)
        img_link_news.append(long_next_url)

    print('---------new link-----------------------')    
    print(img_link_news)

    print('-----------begin large image---------------------')
    collection2 = db.large_image_mars

    for img_link_new in img_link_news:
    #    for x in range(1, 1):
            browser.visit(img_link_new)
            browser.click_link_by_partial_text('Sample')
            html = browser.html
    #        print(html)
            soup_largeimage = bs(html, 'html.parser')
    #        print(soup_largeimage)
            bigger_image = soup_largeimage.find('div', class_='downloads').find('a')['href']
            #.find_by_text('Sample')
            post2 = {
                    'href': bigger_image,
                }
                
            collection2.insert_one(post2)

            print(bigger_image)
            print('--------end large image------------------------')

        # Display items in MongoDB collection
    # large_img_listings = db.large_image_mars.find()

    # for listing in large_img_listings:
    #     print(listing)
