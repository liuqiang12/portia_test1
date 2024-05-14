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


class MovieDoubanCom_1(BasePortiaSpider):
    name = "movie.douban.com_1"
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=25&filter=']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(Top1Item,
                   None,
                   '.item',
                   [Field('field3',
                          '.pic > a > img::attr(src)',
                          []),
                       Field('field1',
                             '.info > .bd > p:nth-child(1) *::text',
                             []),
                       Field('field2',
                             '.info > .bd > .quote > .inq *::text',
                             [])])]]
