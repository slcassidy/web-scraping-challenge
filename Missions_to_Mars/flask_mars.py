# import necessary libraries
from flask import Flask, render_template
# import pymongo
from flask_pymongo import PyMongo

from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

# create instance of Flask app
app = Flask(__name__)

# setup mongo connection
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)
# print(client)

app.config["MONGO_URI"] = "mongodb://localhost:27017/nasa_db"
mongo = PyMongo(app)

# connect to mongo db and collection
# db = client.nasa_db
# collection = db.news
# mongo.db.news


# create route that renders index.html template
@app.route("/")
def echo():
    return render_template("index.html")
    # return render_template("index.html")

@app.route("/scrape")
def echo2():
    news = mongo.db.news.find_one()
    image1 = mongo.db.image_mars.find_one()
    weather_info = mongo.db.weather.find_one()
    return render_template("index.html", text2="Latest News", mars_data=news, 
    img_small=image1, weather=weather_info)

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# def scrape_info():
#     browser = init_browser()

#     # Visit visitcostarica.herokuapp.com
#     url = "https://visitcostarica.herokuapp.com/"
#     browser.visit(url)

#     time.sleep(1)

#     # Scrape page into Soup
#     html = browser.html
#     soup = bs(html, "html.parser")

#     # Get the average temps
#     avg_temps = soup.find('div', id='weather')

#     # Get the min avg temp
#     min_temp = avg_temps.find_all('strong')[0].text

#     # Get the max avg temp
#     max_temp = avg_temps.find_all('strong')[1].text

#     # BONUS: Find the src for the sloth image
#     relative_image_path = soup.find_all('img')[2]["src"]
#     sloth_img = url + relative_image_path

#     # Store data in a dictionary
#     costa_data = {
#         "sloth_img": sloth_img,
#         "min_temp": min_temp,
#         "max_temp": max_temp
#     }

#     # Close the browser after scraping
#     browser.quit()

#     # Return results
#     return costa_data


if __name__ == "__main__":
    app.run(debug=True)