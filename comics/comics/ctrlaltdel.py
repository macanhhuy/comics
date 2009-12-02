from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Ctrl+Alt+Del'
    language = 'en'
    url = 'http://www.ctrlaltdel-online.com/'
    start_date = '2002-10-23'
    history_capable_date = '2002-10-23'
    schedule = 'Mo,We,Fr'
    time_zone = -5
    rights = 'Tim Buckley'

class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        url = 'http://www.cad-comic.com/comics/%(date)s.jpg' % {
            'date': pub_date.strftime('%Y%m%d'),
        }
        return CrawlerResult(url)
