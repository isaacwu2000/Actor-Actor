from get_page_links import get_wikipedia_page_links
search_span = 1

def recursive_link_hopping(url: str, end_url: str, path: list):
    global search_span

    if url==end_url:
        print("\n",path)
    elif len(path) <= search_span:
        links = get_wikipedia_page_links(url)
        for link in links:
            if link not in path:
                print(link, search_span, path)
                recursive_link_hopping(link, end_url, path + [link])
        search_span+=1

if __name__ == "__main__":
    start_actor_url="https://en.wikipedia.org/wiki/Will_Smith"#input("What actor would you like to start from?\nWikipedia Page URL: ")
    end_actor_url="https://en.wikipedia.org/wiki/Jaden_Smith"#input("\nWhat actor would you like to end at?\nWikipedia Page URL: ")

    recursive_link_hopping(start_actor_url, end_actor_url, [start_actor_url])
