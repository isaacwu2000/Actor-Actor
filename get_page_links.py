from bs4 import BeautifulSoup
import requests
import re

def get_wikipedia_page_links(url):
    irrelevant_starts = ['Main_Page','Wikipedia','Help','Special','Talk','File','ISBN']
    relevant_links = set()

    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    for raw_link in soup.find_all('a', attrs={'href': re.compile("^/wiki/")}):
        link = raw_link.get('href')
        link_is_relevant = True
        for start in irrelevant_starts:
            if link.replace("/wiki/","").startswith(start):
                link_is_relevant = False
        if link_is_relevant:
            relevant_links.add(link)

    return relevant_links

print(get_wikipedia_page_links("https://en.wikipedia.org/wiki/Will_Smith"))
