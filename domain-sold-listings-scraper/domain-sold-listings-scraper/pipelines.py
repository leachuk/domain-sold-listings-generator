# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class DomainSoldListingPipeline(object):
    def open_spider(self, spider):
        self.connection = psycopg2.connect("dbname=postgres user=postgres host=localhost")
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("""insert into domain_sold_data(
                              sold_price,
                              sold_date_type,
                              sold_date,
                              sold_type,
                              street_address,
                              city,
                              state,
                              postcode,
                              number_bedrooms,
                              number_bathrooms,
                              number_carparks,
                              square_meters) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                         (item['sold-price'],
                          item['sold-date-type'],
                          item['sold-date'],
                          item['sold-type'],
                          item['street-address'],
                          item['city'],
                          item['state'],
                          item['postcode'],
                          item['number-bedrooms'],
                          item['number-bathrooms'],
                          item['number-carparks'],
                          item['square-meters']))
        self.connection.commit()
        return item
        return item
