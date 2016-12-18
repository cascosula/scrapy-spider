# -*- coding: utf-8 -*-

# Scrapy settings for spidertest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spidertest'
SPIDER_MODULES = ['spidertest.spiders']
NEWSPIDER_MODULE = 'spidertest.spiders'

ITEM_PIPELINES = {'spidertest.pipelines.SpidertestPipeline':1,}
IMAGES_STORE = 'd:\\pics'
