import scrapy

#building type is part of the url query parameter. Run as separate jobs and add type as a db column
class DomainSoldListingSpider(scrapy.Spider):
    name = "domain_soldlisting_spider"
    start_urls = ['https://www.domain.com.au/sold-listings/?postcode=3000']

    def parse(self, response):
        RESULTS_SELECTOR = '.search-results__listing'
        for resultset in response.css(RESULTS_SELECTOR):

            NAME = './/@data-reactid'
            SOLD_PRICE = './/div/div[2]/div[1]/p/text()'
            SOLD_DATE_TYPE = './/div/div[1]/span/text()'  # need to split result into seperate db cols
            STREET_ADDRESS = './/div/div[2]/div[2]/a/h2/span[1]/text()[1]'
            CITY = './/div/div[2]/div[2]/a/h2/span[2]/span[1]/text()'
            STATE = './/div/div[2]/div[2]/a/h2/span[2]/span[2]/text()'
            POSTCODE = './/div/div[2]/div[2]/a/h2/span[2]/span[3]/text()'
            NUMBER_BEDROOMS = './/div/div[2]/div[3]/div/span[1]/span/text()'
            NUMBER_BATHROOMS = './/div/div[2]/div[3]/div/span[2]/span/text()'
            NUMBER_CARPARKS = './/div/div[2]/div[3]/div/span[3]/span/text()'
            SQUARE_METERS = './/div/div[2]/div[3]/div/span[4]/span/text()'  # extract integer value from result 52 m2
            yield {
                'name': resultset.xpath(NAME).extract_first(),
                'sold-price': resultset.xpath(SOLD_PRICE).extract_first(),
                'sold-date-type': resultset.xpath(SOLD_DATE_TYPE).extract_first(),
                'street-address': resultset.xpath(STREET_ADDRESS).extract_first(),
                'city': resultset.xpath(CITY).extract_first(),
                'state': resultset.xpath(STATE).extract_first(),
                'postcode': resultset.xpath(POSTCODE).extract_first(),
                'number-bedrooms': resultset.xpath(NUMBER_BEDROOMS).extract_first(),
                'number-bathrooms': resultset.xpath(NUMBER_BATHROOMS).extract_first(),
                'number-carparks': resultset.xpath(NUMBER_CARPARKS).extract_first(),
                'square-meters': resultset.xpath(SQUARE_METERS).extract_first(),
            }

         #print(resultset)
         #print("USER_AGENT: %s" % self.settings.attributes['USER_AGENT'])
         #print("USER_AGENT_LIST: %s" % self.settings.attributes['USER_AGENT_LIST'])
