import scrapy

class itemSpider(scrapy.Spider):
    name = 'itemSpider'
    start_urls=['http://lab.scrapyd.cn/']

    def parse(self, response):
        mingyan=response.css('div.quote.post')#凡是有空格的在选择器中都用‘.’替代
        for v in mingyan:
            text=v.css('.text::text').extract_first()
            author=v.css('.author::text').extract_first()
            tags=v.css('.tag::text').extract()
            tags=','.join(tags)
            fileName = '%s-语录.txt' % author
            f=open(fileName,'a+')
            f.write(text)
            f.write('\n')
            f.write('标签：' +tags)
            f.close()
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)