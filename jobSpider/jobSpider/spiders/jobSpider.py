import scrapy
from scrapy.http import FormRequest, Request
from ..items import JobspiderItem

class jobSpider(scrapy.Spider):
     name = "jobSpider"
     handle_httpstatus_all = True
     start_urls= ['https://www.linkedin.com/uas/login']

     def parse(self, response):
        token = response.xpath('//form/input[@name = "csrfToken"]/@value').get()
        return FormRequest.from_response(response, formdata={
            'csrfToken':token,
            'session_key' : 'deadlybunshee@gmail.com',
            'session_password' : 'pfeprojet',
            }, callback=self.after_login)

     def after_login(self, response):
        #return Request(url='https://www.linkedin.com/jobs/search/?keywords=&location=&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0', callback=self.startScraping)

        return Request(url='https://www.linkedin.com/jobs/search/?geoId=&location=&start=850', callback=self.startScraping)

     def startScraping(self, response):
         items = JobspiderItem()
         for post in response.xpath('//div[@class = "base-search-card__info"]'):
             try :
                 jobTitle =  post.xpath('.//h3[@class = "base-search-card__title"]/text()').get().strip(' \n\t\u2013'),
                 companyName = post.xpath('.//h4[@class = "base-search-card__subtitle"]/a/text()').get().strip(' \n\t\u2013'),
                 jobPlace = post.xpath('.//span[@class = "job-search-card__location"]/text()').get().strip(' \n\t\u2013'),
                 #date = response.css('time::attr(datetime)').get(),
                 date = response.xpath(
                     './/li[@class = "job-card-container__listed-time job-card-container__footer-item"]/text()').get()

             except :
                 jobTitle =  post.xpath('.//h3[@class = "base-search-card__title"]/text()').get().strip(' \n\t\u2013'),
                 companyName = post.xpath('.//h4[@class = "base-search-card__subtitle"]/a/text()').get().strip(' \n\t\u2013'),
                 jobPlace = post.xpath('.//span[@class = "job-search-card__location"]/text()').get().strip(' \n\t\u2013'),
                 #date = response.css('time::attr(datetime)').get(),
                 date = response.xpath('.//li[@class = "job-card-container__listed-time job-card-container__footer-item"]/text()').get()
             items['jobTitle'] = jobTitle
             items['companyName'] = companyName
             items['jobPlace'] = jobPlace
             items['date'] = date
             items['source'] = 'linkedin'
             yield items


#import scrapy
#from scrapy.spider import BaseSpider
#from scrapy.selector import HtmlXPathSelector
#from scrapy.http import Request
#from scrapy.http import FormRequest