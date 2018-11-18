import scrapy


class ScraperSpider(scrapy.Spider):
    name = "domain_soldlisting_spider"
    start_urls = ['https://www.domain.com.au/sold-listings/?postcode=3000']

    def parse(self, response):
        #print("Existing settings: %s" % self.settings.attributes.keys())
         print("USER_AGENT: %s" % self.settings.attributes['USER_AGENT'])
         print("USER_AGENT_LIST: %s" % self.settings.attributes['USER_AGENT_LIST'])
