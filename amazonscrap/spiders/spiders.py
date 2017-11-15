from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from amazonscrap.items import AmazonscrapItem
import scrapy

class MySpider(scrapy.Spider):
	name = "adidas"
	
	start_urls = ['https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=adidas+shoes']
	
 	def parse(self, response):
  		items = AmazonscrapItem()
		title = response.xpath('//a[@class ="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@title').extract_first()	#extracting name
  		prices = response.xpath('//*[@id="priceblock_ourprice"]/@text').extract_first()	#extracting price
  		src = response.xpath('//img[@class ="s-access-image cfMarker"]/@src').extract_first()	#extracting image
		href = response.xpath('//a[@class ="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@href').extract_first()	#extracting description		
		items['name'] = ','.join(title).strip()
		items['price'] = ','.join(prices).strip()
		items['image'] = ','.join(src).strip()
		items['description'] = ','.join(href).strip()
	
		yield items
		
		
		
		
		
		
	
		


			