import scrapy

class IndeedItem(scrapy.Item):

    jobTitle = scrapy.Field()
    companyName = scrapy.Field()
    jobPlace = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
