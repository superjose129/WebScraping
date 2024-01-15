import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
url = "http://s7.kanesherwell.com/insights/"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant information from the HTML code
movies = []
for row in soup.select('.blog-feed__item__content1'):
        
    title_elements = row.select('h5', class_= 'blog-feed__item__title')
    content_elements = row.select('div', class_= 'blog-feed__item__content')

    titles = [title.text for title in title_elements]
    contents = [content.text.replace('\n', '') for content in content_elements]
    # contents = [content.text for content in content_elements]


    for title, content in zip(titles, contents):
        movies.append([title, content])

# Store the information in a pandas dataframe
df = pd.DataFrame(movies, columns=['Title', 'Content'])

# Add a delay between requests to avoid overwhelming the website with requests
time.sleep(1)

# Convert as a string
# df_string = df.to_string(index=False)
# Export the data to a CSV 
df.to_csv('scrapein.csv', index=False)
# Read the CSV file into a string
# with open('scrape.csv', 'w') as file:
#     file.write(df_string)

# Print the CSV string
print(df)