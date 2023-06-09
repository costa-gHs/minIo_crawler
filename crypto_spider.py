import scrapy
import os

li_content = ""

class CryptoSpider(scrapy.Spider):
    name = 'crypto_spider'
    start_urls = ['https://www.google.com/finance/markets/cryptocurrencies?hl=pt']

    def parse(self, response):
        ul = response.xpath('//ul')
        lis = ul.xpath('.//li')
        for li in lis:
            li_content = li.get()
            print(li_content)

            if os.path.exists('dados.txt'):
                append_write = 'a'
            else:
                append_write = 'w'

            with open('dados.txt', append_write) as arquivo:
                arquivo.write(li_content + '\n')
