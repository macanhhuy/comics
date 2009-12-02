from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Bizarro'
    language = 'no'
    url = 'http://underholdning.no.msn.com/tegneserier/bizarro/'
    start_date = '1985-01-01'
    history_capable_days = 12
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = 1
    rights = 'Dan Piraro'

class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        feed = self.parse_feed(
            'http://underholdning.no.msn.com/rss/bizarro.aspx')
        for entry in feed.for_date(pub_date):
            url = entry.enclosures[0].href
            return CrawlerResult(url)
