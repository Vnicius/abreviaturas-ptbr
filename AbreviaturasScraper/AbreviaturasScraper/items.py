# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AbreviaturasscraperItem(scrapy.Item):
    abrev= scrapy.Field()
    desc= scrapy.Field()
