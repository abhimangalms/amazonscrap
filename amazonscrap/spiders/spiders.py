from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from amazonscrap.items import AmazonscrapItem

class MySpider(BaseSpider):
	name = "adidas"
	allowed_domains = ["amazon.in"]
	start_urls = ["https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=adidas"]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//p")
		items = []
		for titles in titles:
			item = AmazonscrapItem()
			item ["title"] = titles.select("a/text()").extract()
			item ["link"] = titles.select("a/@href").extract()
			items.append(item)
		return items