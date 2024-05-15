import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    name = "book_crawl"
    allowed_domains = ["hanbit.co.kr"]
    start_urls = ['https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=001',
                'https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=002',
                'https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=003',
                'https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=004',
                'https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=005',
                'https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=006',
                'https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=007',
                'https://m.hanbit.co.kr/store/books/category_list.html?cate_cd=008',]

    rules = (Rule(LinkExtractor(allow=r'store/books/look.php\?p_code=.*'), callback="parse_item", follow=True),
            Rule(LinkExtractor(allow=
                            r'store/bppks/category_list\.html\?page=\d+&cate_cd=00\d+&&srt=p_pub_date')))

    def parse_item(self, response):
        i = {}
        i["book_title"] = response.xpath(
            '\\*[@id="container]/div[1]/div[1]/div[1]/div[2]/h3/text()').extract()
        
        i['book_author'] = response.xpath(
            '\\*[@id="container]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="저자 : "]/span/text()'
        ).extract()
        
        i['book_author'] = response.xpath(
            '\\*[@id="container]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="번역 : "]/span/text()'
        ).extract()
        
        i['book_author'] = response.xpath(
            '\\*[@id="container]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="출간 : "]/span/text()'
        ).extract()
        
        i['book_author'] = response.xpath(
            '\\*[@id="container]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="ISBN : "]/span/text()'
        ).extract()
        return i
