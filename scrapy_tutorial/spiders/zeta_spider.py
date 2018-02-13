import scrapy


def gen_search_urls(search_term, max_pages):
    """Create a list of URLs for a search on Zeta to pass to start_urls."""
    url_list = []
    url_list.append('http://zetatijuana.com/?s=%s' % search_term)
    if max_pages > 1:
        for page_number in range(2, max_pages + 1):
            url_list.append('http://zetatijuana.com/page/%s/?s=%s'
                            % (page_number, search_term))
    return url_list


class UrlSpider(scrapy.Spider):
    name = 'zeta_urls'

    start_urls = gen_search_urls('narcomanta', 10)

    def parse(self, response):
        urls = response.css('div.nota-cat').css('a::attr(href)').extract()
        filename = 'new_urls.txt'
        with open(filename, 'a') as file_out:
            for url in urls:
                file_out.write(url)
                file_out.write('\n')
            # file_out.write(url)



class QuotesSpider(scrapy.Spider):
    name = "zeta"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
