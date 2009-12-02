# encoding: utf-8

from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Pondus (db.no)'
    language = 'no'
    url = 'http://www.dagbladet.no/tegneserie/pondus/'
    start_date = '1995-01-01'
    history_capable_days = 14
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = 1
    rights = 'Frode Øverli'

class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        url = 'http://www.dagbladet.no/tegneserie/pondusarkiv/serve.php?%(date)s' % {
            'date': self.date_to_epoch(pub_date),
        }
        return CrawlerResult(url)
