from bs4 import BeautifulSoup
import requests
import re

def get_wikipedia_page_links(url: str)->list:
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
            relevant_links.add("https://en.wikipedia.org" + link)

    return list(relevant_links)