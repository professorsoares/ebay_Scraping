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
		bloco_produtos = soup.find('div', id='srp-river-results')
	except:
		bloco_produtos = ""


	try:
		if bloco_produtos  != "":
			links = bloco_produtos.find_all("a", {"class": "s-item__link"})
		else:
			links = []
	except:
		links = []

	urls = [item.get('href') for item in links]

	print(urls)
	print('1: -------------------------------------------')

	# try:
	# 	products = soup.find_all('div', class_="s-item__wrapper clearfix")
	# except:
	# 	products = []
	#
	# product_name = [item.find('h3') for item in products]
	#
	# print(product_name[0].text)

	return urls

def main():

	# Busca a lista de Produtos
	url_lista_relogios = 'https://www.ebay.com/sch/i.html?_nkw=watches+for+men&_pgn=2'
	soup = get_page(url_lista_relogios)
	products = get_index_data(soup)

	# Pega o link de cada produto para buscar os dados desse produto
	for link in products:
		print("LINK: " + link)
		data = get_detail_data(get_page(link))
		print(data)
	
if __name__ == '__main__':
	main()