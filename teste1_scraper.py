#ebay_scraper.py

# Vídeo: https://www.youtube.com/watch?v=m4hEAhHHykI

#pip install requests beautifulsoup4 lxml


# TODO:
# 1. Make a request
# 2. Collect data from each detail
# 3. Collect all linksto detail pages of each product
# 4. Write scraped data to a csv file


import requests
from bs4 import BeautifulSoup


def get_page(url):
	response = requests.get(url)
	print(response.ok)
	print(response.status_code)
	if not response.ok:
		print('Server responded:', response.status_code)
	else: 
		soup = BeautifulSoup(response.text, 'lxml')
		return soup


def get_detail_data(soup):
	#title
	#price
	#items sold
	
	title = soup.find('h1').find('span').text
	print('PRODUCT: ' + str(title))

	try:
		priceContent = soup.find('span', id='prcIsum').text.strip()
		currency, price = priceContent.split(" ")
	except:
		price = ''
	print('PRICE: ' + str(price))

	try:
		sold = soup.find('a', class_="vi-txt-underline").text.split(" ")[0]
	except:
		sold = ''
	print('Total Sold: ' + str(sold) + " já vendidos")

	data = {
		'title':title,
		'price':price,
		'items_sold':sold
	}
	return data


def get_index_data(soup):
	try:
		# product_name = soup.find_all('h3') # WORKING!
		#product_name = soup.find_all('div', class_="s-item__wrapper clearfix").find('div').find('a').find('h3').count
		#product_name = soup.find_all('h3', class_="s-item__title")
		#product_name = soup.find_all('div', class_="s-item__info clearfix")

		links = soup.find_all("a", {"class": "s-item__link"})

	except:
		links = []

	urls = [item.get('href') for item in links]
	print(len(links))
	print('1: -------------------------------------------')
	print(urls)


def main():

	# Segunda chamada: Lista de relógios:
	url_lista_relogios = 'file:///C:/git/ebay_Scraping/teste1.htm'
	soup = get_page(url_lista_relogios)
	get_index_data(soup)
	
	
if __name__ == '__main__':
	main()