# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
from bs4 import BeautifulSoup as bs
import os
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# %%
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# URL of page to be scraped
url = "https://redplanetscience.com/"


# %%
browser.visit(url)


# %%
# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = bs(html, 'html.parser')


# %%
# Examine the results, then determine element that contains sought info
# print(soup.body.prettify())


# %%
# Find the PARENT DIV and print title
Title = soup.find_all('div', class_='list_text')[
    0].find('div', class_='content_title').text
print('**************************************')
print('Title')
print(Title)


# %%
# print latest news Paragraph
Article = soup.find_all('div', class_='list_text')[0].find(
    'div', class_='article_teaser_body').text
print('**************************************')
print('Article')
print(Article)

# %%


# %%
url1 = 'https://spaceimages-mars.com/'
browser.visit(url1)


# %%
html1 = browser.html
soup1 = bs(html1, 'html.parser')


# %%
# print(soup1.body.prettify())


# %%
featured_image_url = soup1.find("div", class_="header").find(
    "div", class_="floating_text_area").a.get("href")
print('**************************************')
print('featured_image_url')
print(featured_image_url)

# %%


# %%
url2 = "https://galaxyfacts-mars.com/"


# %%
tables = pd.read_html(url2)
print('**************************************')
print('tables')
print(tables)

# %%
df = tables[0]
df.head()


# %%
html_table = df.to_html()
print('**************************************')
print('html_table')
print(html_table)

# %%


# %%
url3 = "https://marshemispheres.com/"


# %%
browser.visit(url3)


# %%
html2 = browser.html
soup2 = bs(html2, 'html.parser')


# %%

# print(soup2.body.prettify())


# %%
hemisphere_image_urls = []


# %%


# %%

html2 = browser.html
soup2 = bs(html2, 'html.parser')

images = soup2.find_all(
    'div', class_='item')
print(images)
for item in images:
    print(item.img.get('src'))
    print(
        item.div.a.h3.text

    )
    hemisphere_image_urls.append({
        'img_url': item.img.get('src'),
        'title': item.div.a.h3.text
    })
print(hemisphere_image_urls)
exit(0)



# %%
# hemisphere_image_urls


# %%
hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere Enhanced",
     "img_url": "https://marshemispheres.com/images/full.jpg"},
    {"title": "Schiaparelli Hemisphere Enhanced",
     "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere Enhanced",
     "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
    {"title": "Valles Marineris Hemisphere Enhanced",
     "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"}
]


# %%


# %%


# %%


# %%


# %%
