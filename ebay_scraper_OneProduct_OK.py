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
	print('Total vendidos: ' + str(sold) + " já vendidos")

	data = {
		'title':title,
		'price':price,
		'items_sold':sold
	}
	return data


def main():
	print('-------------------------------------------')

	url = 'https://www.ebay.com/itm/174966171523?epid=28020141486&hash=item28bccbe783:g:81cAAOSwC7JhXMmD&amdata=enc%3AAQAHAAAA8GoR7i%2Bib2yNGNP5h9to61anQ3jlclrDEp6IYhIwB52KkqYxzHQOuFTRb2tVHUnZAz%2FAZXnko9Mi6K1Imwo6TTSIlEi1gsEQTx27TKPdrencmbal2rO4p6U9gKwVEZ8qRClD6rk2G0VtjtxFLPGob90sbqZ23cbuHjgkCUOPrjMDw2L00BS0ZaqCyomrBxSj6Mo43djPj88tiulfQaFupPDR2Y9o83mSnYeGeEwfC1zXGA3wdVQnnfj7yk8XvZy%2BtN86gmphhVkyMuBN6HCP8WZs1IZqJOJPS88cDIx8%2F2xIyV8%2BF60dHCOqqgZnm64KCg%3D%3D%7Ctkp%3ABFBM_u3cx8Fg' # Link of detail page
	soup = get_page(url)
	get_detail_data(soup)

	print('-------------------------------------------')


if __name__ == '__main__':
	main()