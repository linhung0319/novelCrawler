import scrapy

class NovelSpider(scrapy.Spider):
    name = "novel"
    start_urls =[
        'https://www.novel543.com/'
    ]

    def parse(self, response):
        for novel in response.css('ul.hot li'):
            yield {
                'cover_image': novel.css('a.bookimg img::attr(data-original)').get(),
                'title': novel.css('a:nth-of-type(2)::attr(title)').get(),
                'author': novel.css('a.light::text').get()
            }