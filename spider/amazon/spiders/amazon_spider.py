#-*- coding: UTF-8 -*- 

import scrapy
import time

#fn1 = "comm.txt"
#fn2 = "rate.txt"
#f1 = open(fn1,'wb')
#f2 = open(fn2,'wb')
'''
class QuotesSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.cn"]
    #delay time = 4s

    start_urls = ['https://www.amazon.cn/product-reviews/B01ER1SYT6/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber={}'.format(i) for i in range(1,11)]
                    
    def parse(self, response):
        if response.status!=200:
            time.sleep(60)
            yield Request(response.url,meta=response.meta,callback=self.parse,dont_filter=True)
        filenamee = "test.html"
        page = response.url.split("/")[-2]
        num = response.url.split("/")[-1][-1]
        fn1 = 'com-%s-%s.txt' % (page,num)
        fn2 = 'rate-%s-%s.txt' % (page,num)
        with open(filenamee,'wb') as ff:
            ff.write(response.body)
        f1 = open(fn1,'wb')
        f2 = open(fn2,'wb')
        t1 = response.xpath('//span[contains(@data-hook,"review-body")]/text()').extract()
        t2 = response.xpath('//i[contains(@data-hook,"review-star-rating")]/span[contains(@class,"a-icon-alt")]/text()').extract()
        delay = len(t2) - len(t1)
        for count in range(0,len(t1)):
            content = t1[count]+'\n'
            rate = t2[count+delay]+'\n'
            print(content)
            f1.write(content.encode('utf-8'))
            f2.write(rate.encode('utf-8'))
'''
fn1 = "url.txt"
f1 = open(fn1,'wb')
class UrlSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.cn"]
    #delay time = 4s

    #start_urls = ['https://www.amazon.cn/s/ref=sr_ex_n_1?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051%2Cp_6%3AA1AJ19PSB66TGU&bbn=2152154051&sort=date-desc-rank&ie=UTF8&qid=1506741940']
    #start_urls = ['https://www.amazon.cn/s/ref=sr_st_popularity-rank?fst=as%3Aoff&rh=n%3A2016156051%2Cn%3A!2016157051%2Cn%3A2152154051%2Cp_6%3AA1AJ19PSB66TGU%2Cn%3A2154351051&qid=1506744036&__mk_zh_CN=亚马逊网站&bbn=2152154051&sort=popularity-rank']
    start_urls = ['https://www.amazon.cn/s/ref=sr_pg_3?fst=as%3Aoff&rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051%2Cp_6%3AA1AJ19PSB66TGU%2Cn%3A2154351051&page={}'.format(t) for t in range(1,15)]
    def parse(self, response):
        p = response.xpath('//a[contains(@class,"a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal")]/@href').extract()
        if len(p) == 0:
            time.sleep(1)
            yield scrapy.http.Request(response.url,meta=response.meta,callback=self.parse,dont_filter=True)
        #if response.status!=200:
        #    time.sleep(60)
        #    yield Request(response.url,meta=response.meta,callback=self.parse,dont_filter=True)
        #p = response.xpath('//a[contains(@class,"a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal")]/@href').extract()
        
        #for it in range(1,6):
        #    print('\n')
        #print(len(p))
        #f1.write(len(ttt))
        for shop_url in p:
            print(shop_url)
            content = "'"+shop_url+"',\n"
            f1.write(content)
            #yield Request(shop_url,callback = self.shop_parse)
