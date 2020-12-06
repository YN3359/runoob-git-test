import scrapy

class itemSpider(scrapy.Spider):
    name = 'ggSpider'
    start_urls=['http://www.miit.gov.cn/datainfo/resultSearch?searchType=advancedSearch&categoryTreeId=1128&pagenow=2']

    def parse(self, response):
        chexing=response.css('table.table.table-bordered.table-responsive tbody tr')#凡是有空格的在选择器中都用‘.’替代
        for v in chexing:
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