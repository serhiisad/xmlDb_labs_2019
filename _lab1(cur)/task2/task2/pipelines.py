# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import lxml.html
from lxml import etree


class Task2Pipeline(object):

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):

        xslt_doc = etree.parse("./spiders/items.xslt")
        xslt_transformer = etree.XSLT(xslt_doc)

        source_doc = etree.parse("./spiders/tennis-shoes.xml")
        output_doc = xslt_transformer(source_doc)

        output_doc.write("output-doc.html", pretty_print=True)

