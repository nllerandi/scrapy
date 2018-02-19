# -*- coding: utf-8 -*-
import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = 'headlines'
    allowed_domains = ['https://www.verizonwireless.com/']
    start_urls = ['https://www.verizonwireless.com/']

    def parse(self, response):
        headlines = response.xpath('//*[@class="homepage-heading"]/text()').extract()
        for headline in headlines:
        	print(headline)	
        # yield {"Headline": headline}
	
