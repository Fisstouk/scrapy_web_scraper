import scrapy

class ali_spiders(scrapy.Spider):
    name = "ali"

    def start_requests(self):
        urls = [
            'https://pt.aliexpress.com/category/201005406/special-store.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'ali-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

    def parse_html(self, response):
        for quote in response.css('div.quote'):
            yield {
                '_1tu1Z Vgu6S': ali.css('span._1tu1Z Vgu6S::text').get(),
                'mGXnE _37W_B': ali.css('small.mGXnE _37W_B::text').get(),
            }