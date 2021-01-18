from typing import List
import requests

from bs4 import BeautifulSoup

def get_soup(url):
    print(f"get_soup({url})")
    headers = {'User-Agent':'Mozilla/5.0'}
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_random_page_url():
	page = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary").json()
	title = page["title"]
	description = page["extract"]
	url = page["content_urls"]["desktop"]["page"]

	# Uncomment to print information about the page
		# print(f"Title: {title}")
		# print(f"Description: {description}")
		# print(f"URL: {url}")

	return url

def get_all_links(soup):
	links = []
	for link in soup.find_all('a'):
		l = link.get('href')
		if "/wiki/" in str(l):
			# print(l)
			links.append(str(l))

	return links


def store(page_name, links):
	# Store in either: Database (MongoDB) or Excel
	pass

def run():
	url = get_random_page_url()
	page = get_soup(url)
	links = get_all_links(page)
	print(links)






run()








