from comics.aggregator.crawler import CrawlerBase, CrawlerResult
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Three Panel Soul'
    language = 'en'
    url = 'http://www.threepanelsoul.com/'
    start_date = '2006-11-05'
    history_capable_days = 180
    time_zone = -5
    rights = 'Ian McConville & Matt Boyd'

class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        feed = self.parse_feed('http://www.rsspect.com/rss/threeps.xml')
        for entry in feed.for_date(pub_date):
            url = entry.summary.src('img')
            title = entry.title
            text = entry.summary.alt('img')
            return CrawlerResult(url, title, text)
