from datetime import datetime, timedelta

import scrapy
from ..items import IndeedItem

class indeedSpider(scrapy.Spider):
     name = "indeed"
     handle_httpstatus_all = True
     start_urls = ['https://indeed.com/jobs?q=All%20Jobs&vjk=c2845500eb238fd3']

     def parse(self, response):
         items = IndeedItem()
         for post in response.xpath('//div[@class = "job_seen_beacon"]'):
             if (post.xpath('.//span[@class = "companyName"]/text()').get() is None):
                 jobTitle = post.xpath('.//h2/span/text()').get(),
                 companyName = post.xpath('.//span[@class = "companyName"]/a/text()').get(),
                 jobPlace = post.xpath('.//div[@class = "companyLocation"]/text()').get()#extract(),
                 date = post.xpath('.//span[@class ="date"]/text()').get(),
                 emp_str = ""
                 for m in date[0]:
                     if m.isdigit(): #['0','1','2','3','4','5','6','7','8','9']:
                         emp_str = emp_str + m
                 if emp_str.isdigit():
                    final_t = int(emp_str)
                 final=final_t
                 d = datetime.today() - timedelta(days=final)
             else :
                 jobTitle =  post.xpath('.//h2/span/text()').get(),
                 companyName = post.xpath('.//span[@class = "companyName"]/text()').get(),
                 jobPlace = post.xpath('.//div[@class = "companyLocation"]/text()').get()#extract(),
                 date = post.xpath('.//span[@class ="date"]/text()').get(),
                 emp_str = ""
                 for m in date[0]:
                     if m.isdigit():  #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                         emp_str = emp_str + m
                 if emp_str.isdigit():
                    final_t= int(emp_str)
                 final = final_t
                 d = datetime.today() - timedelta(days=final)
             #user = indeedSpider()
             items['jobTitle'] = jobTitle
             items['companyName'] = companyName
             items['jobPlace'] = jobPlace
             items['date'] = d
             items['source'] = 'indeed'
             yield items
