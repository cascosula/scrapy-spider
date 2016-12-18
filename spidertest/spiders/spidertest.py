# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
from bs4 import BeautifulSoup
from spidertest.items import SpidertestItem
from scrapy.selector import Selector

class SpiderTest(scrapy.Spider):
	name = "spidertest"
	allowed_domains = ["taipics.com"]
	start_urls = ('http://taipics.com',)

	def parse(self, response):
		#mainContent = BeautifulSoup(response.body, "lxml").select('div[id="content"]')[0]
		
		#for img in mainContent.select('img[src^="images/"]'):
			#yield scrapy.Request(url_query+img['src'], self.parse_image)
			#return self.build_image_item(url_query+img['src'],img['src'].split("/")[-1])
			#yield self.build_image_item(url_query+img['src'],img['src'].split("/")[-1])]
		domain = u'http://taipics.com/'
		#print response.css('a::attr(href)').extract()
		for link in response.css('a::attr(href)').extract():
			if "php" in link :
				#print ("###link###", domain+link)
				#return scrapy.Request(domain+link, self.parse_image)
				yield scrapy.Request(domain+link, self.parse_image)
		#for img in response.css('img'):
		#	item = SpidertestItem()
		#	srcs = img.xpath('@src').extract()
		#	item['image_urls'] = [url_query+src for src in srcs]
		#	item['image_name'] = srcs[0].split("/")[-1]
		#	#return item
		#	yield item
		
	def parse_image(self, response):
		for src in response.css('img').xpath('@src').extract():
			if "image" in src:
				item = SpidertestItem()
				item['image_urls'] = [u'http://taipics.com/'+src]
				item['image_domain'] = u'taipics.com'
				item['image_category'] = response.css('h1::text').extract()[0]
				item['image_name'] = src.split("/")[-1]
				#print item
				#return item
				yield item

	def build_image_item(self, url, name):
		item = SpidertestItem()
		item['image_name'] = name
		item['image_urls'] = [url]
		return item