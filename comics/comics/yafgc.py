from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Yet Another Fantasy Gamer Comic'
    language = 'en'
    url = 'http://yafgc.shipsinker.com/'
    start_date = '2006-05-29'
    history_capable_date = '2006-05-29'
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -8
    rights = 'Rich Morris'

class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        url = ('http://yafgc.shipsinker.com/istrip_files/strips/%s.jpg' %
            pub_date.strftime('%Y%m%d'))
        return CrawlerResult(url)
