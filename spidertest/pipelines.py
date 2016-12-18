# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

class SpidertestPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			#print ("requesting image : ",image_url)
			yield Request(image_url, meta={'item': item})
			
	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			#print "image download failed"
			raise DropItem("Item contains no images")
		return item
		
	def file_path(self, request, response=None, info=None):
		item = request.meta['item']
		filename = u'full/%s/%s/%s.jpg' % (item['image_domain'], item['image_category'], item['image_name'])
		return filename
