# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedItem(scrapy.Item):
    # define the fields for your item here like:
    jobTitle = scrapy.Field()
    companyName = scrapy.Field()
    jobPlace = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()