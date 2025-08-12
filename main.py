from get_page_links import get_wikipedia_page_links
import time

def connect_actors(start_actor_url: str, end_actor_url: str):
    # Modified Dijkstra's algorithm implementation
    to_visit = []
    visited_urls = []
    searching = True

    # Setup — Running algorithm for source
    initial_links = get_wikipedia_page_links(start_actor_url)
    for link in initial_links:
        to_visit.append({"url":link, "path":[start_actor_url]+[link]})

    # Iteratively expanding search
    while searching:
        page = to_visit[0]
        page_links = get_wikipedia_page_links(page['url'])
        for link in page_links:
            if link==end_actor_url:
                return (page['path']+[link])
            else:
                if link not in visited_urls: # Preventing duplicates in visited pages               
                    to_visit.append({"url":link, "path":page['path']+[link]})
        to_visit.remove(page)
        visited_urls.append(page["url"])


if __name__ == "__main__":
    start_actor_url=input("What actor would you like to start from?\nWikipedia Page URL: ")
    end_actor_url=input("\nWhat actor would you like to end at?\nWikipedia Page URL: ")
    print("\n"+"Path: "+str(connect_actors(start_actor_url, end_actor_url)))