from bs4 import BeautifulSoup
import requests
import re

def get_page_links(url):
    links = []
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))
    
    return links

print(get_page_links("https://www.geeksforgeeks.org/courses"))
