import requests
from bs4 import BeautifulSoup
import pprint
import sys

_URL = 'https://news.ycombinator.com/news'
_VOTE_THRESHOLD = 100

def get_soup_object_for_page(url):
    res = requests.get(url)
    soup_obj = BeautifulSoup(res.text, "html.parser")
    return soup_obj

def get_more_url(soup):
    more = soup.select('.morelink')
    if more != None:
        url = _URL + soup.select('.morelink')[0].get('href', None)
    return url

def get_links(spans):
    links = []
    for span in spans:
        link = span.select('a')[0]
        links.append(link)
    return links


def create_filtered_hn(links, subtext):
    filter_hn = []
    for i, link in enumerate(links):
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].text.split(' ')[0])
            if points > _VOTE_THRESHOLD:
                link = links[i]
                title = link.getText()
                href = link.get('href', None)
                filter_hn.append({'title': title, 'link':href, 'votes': points})
    return filter_hn

def sort_by_votes(hn):
    return (sorted(hn, key=lambda k:k['votes'], reverse=True))


def main(args):

    hn =[]
    soup = None
    url = _URL
    page = 0
    while page < args[0]:
        pprint.pprint(f"Processing Page {page} - {url}" )
        soup = get_soup_object_for_page(url)
        #select links and votes
        spans = soup.select('.titleline')
        links = get_links(spans)
        subtext = soup.select('.subtext')
        # append fileterd list to complete list
        hn = hn + create_filtered_hn(links, subtext)

        #get next page URL
        url = get_more_url(soup)
        page += 1
    # sort all links by page
    hn = sort_by_votes(hn)
    pprint.pprint(hn)


if __name__ == '__main__':
#  sys.exit(main(sys.argv[1:]))
  sys.exit(main([2]))
