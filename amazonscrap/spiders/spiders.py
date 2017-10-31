from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from amazonscrap.items import AmazonscrapItem
import scrapy

class MySpider(scrapy.Spider):
	name = "adidas"
	allowed_domains = ["amazon.in"]
  
  #Use working product URL below
  	start_urls = ["https://www.amazon.in/s/ref=nb_sb_ss_i_2_7?url=search-alias%3Dshoes&field-keywords=adidas+shoes&sprefix=adidas+%2Cundefined%2C353&crid=O7E4NE6341EK"]
 
 	def parse(self, response):
  		items = AmazonscrapItem()
  		title = response.xpath('//h2[@class="s-access-title"]/span/text()').extract()	#extracting name
  		sale_price = response.xpath('//span[contains(@id,"s-price")]/text()').extract()	#extracting price
  		src = response.xpath('//img[@class="s-access-image cfMarker"]/@src').extract()	#extracting image
		href = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()	#extracting description
  		
  		items['name'] = ''.join(title).strip()
  		items['price'] = ''.join(sale_price).strip()
  		items['image'] = ''.join(src).strip()
		items['description'] = ''.join(href).strip()
		yield items

			