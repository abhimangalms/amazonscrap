from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from amazonscrap.items import AmazonscrapItem
import scrapy

class MySpider(scrapy.Spider):
	name = "adidas"
	#allowed_domains = ["amazon.in"]
  
  	start_urls = ['https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=adidas+shoes']
	
 
 	def parse(self, response):
  		items = AmazonscrapItem()
		title = response.xpath('//div//a[@class ="a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal"]/@title').extract()	#extracting name
  		sale_price = response.xpath('//span[@class ="a-size-base.a-color-price.s-price.a-text-bold"]/@text').extract()	#extracting price
  		src = response.xpath('//img[@class ="s-access-image cfMarker"]/@src').extract()	#extracting image
		href = response.xpath('//div//a[@class ="a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal"]/@href').extract()	#extracting description
  		
  		items['name'] = ','.join(title).strip()
  		items['price'] = ','.join(sale_price).strip()
  		items['image'] = ','.join(src).strip()
		items['description'] = ','.join(href).strip()
		yield items
		
		
	
		


			