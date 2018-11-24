import scrapy


class DomainSoldListingSpider(scrapy.Spider):
    name = "domain_soldlisting_spider"
    start_urls = ['https://www.domain.com.au/sold-listings/?postcode=3000']

    def parse(self, response):
        RESULTS_SELECTOR = '.search-results__listing'
        for resultset in response.css(RESULTS_SELECTOR):

            NAME = './/@data-reactid'
            STREET_ADDRESS = './/div/div[2]/div[2]/a/h2/span[1]/text()[1]'
            SOLD_PRICE = './/div/div[2]/div[1]/p/text()'
            yield {
                'name': resultset.xpath(NAME).extract_first(),
                'sold-price': resultset.xpath(SOLD_PRICE).extract_first(),
                'street-address': resultset.xpath(STREET_ADDRESS).extract_first(),
            }

         #print(resultset)
         #print("USER_AGENT: %s" % self.settings.attributes['USER_AGENT'])
         #print("USER_AGENT_LIST: %s" % self.settings.attributes['USER_AGENT_LIST'])
