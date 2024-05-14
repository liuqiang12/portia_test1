from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import TopItem, Top1Item, PortiaItem


class MovieDouban(BasePortiaSpider):
    name = "movie.douban.com"
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=25&filter=']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(TopItem, None, 'body > div > div:nth-child(1), body > div > div:nth-child(1) > div', [Field(None,
                                                                                                               '.lnk-doubanapp *::text, .nav-search > form > fieldset *::text, div > .lnk-doubanapp *::text, div > .nav-search > form > fieldset *::text', [])])]]
