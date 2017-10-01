#-*- coding: UTF-8 -*- 

import scrapy
'''
fn1 = "comm.txt"
fn2 = "rate.txt"
f1 = open(fn1,'wb')
f2 = open(fn2,'wb')

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

fn1 = "review_url.txt"
f1 = open(fn1,'wb')
class ReviewsSpider(scrapy.Spider):
    name = "amazon_review"
    allowed_domains = ["amazon.cn"]
    #delay time = 4s

    #start_urls = ['https://www.amazon.cn/s/ref=sr_ex_n_1?rh=n%3A2016156051%2Cn%3A%212016157051%2Cn%3A2152154051%2Cp_6%3AA1AJ19PSB66TGU&bbn=2152154051&sort=date-desc-rank&ie=UTF8&qid=1506741940']
    #start_urls = ['https://www.amazon.cn/Futex-Pro-%E5%A5%B3%E5%BC%8F-%E8%BF%90%E5%8A%A8%E7%9F%AD%E8%A2%96%E5%9C%86%E9%A2%86T%E6%81%A4-171000004B-%E6%B7%B1%E7%81%B0%E9%98%B3%E7%A6%BB%E5%AD%90-%E9%BB%91%E8%89%B2-XXL-175-96A/dp/B071J1656G/ref=sr_1_5?m=A1AJ19PSB66TGU&s=apparel&ie=UTF8&qid=1506753176&sr=1-5&nodeID=2154351051&psd=1']
    def parse(self, response):
        f2 = open("ttt.html",'wb')
        f2.write(response.body)
        if response.status !=200:
            time.sleep(60)
            yield Request(response.url,meta=response.meta,callback=self.parse,dont_filter=True)
        t1 = response.xpath('//a[contains(@data-hook,"see-all-reviews-link")]/@href').extract()
        #for count in range(1,5):
        #    print("\n")
        #print(len(t1))
        if(len(t1) != 0):
            for p_number in range(1,10):
                review_url = "'"+t1[0]+"',\n"
                f1.write(review_url)

