import re
from urllib.parse import urljoin

from keeptrackd import (
        browser,
        dbmanager,
        tracker
        )


class WebAceTracker(tracker.common.Tracker):

    valid_url_re = re.compile(r'https?://web-ace.jp/youngaceup/contents/.+$')

    def __init__(self, url):
        self.url = url
        self.browser = browser.Browser()
        self.db = dbmanager.DBManager()

    @classmethod
    def suitable(cls, url):
        return cls.valid_url_re.match(url) is not None

    def check_update(self):
        latest = self._get_latest()
        last_time = self._get_last_time()
        if not last_time or latest != last_time:
            self._save(latest)
            return True
        return None

    def postprocess(self):
        print(self.url)

    def _get_latest(self):
        self.browser.get(self.url)
        self.page_source = self.browser.page_source
        self.latest = self.browser.find_element_by_css_selector('#read > div.inner.align-left.inner-news > ul > li:first-child > a > div > div > p').text
        return self.latest

    def _get_last_time(self):
        result = self.db.get(self.url)
        if result:
            return result[1]
        return None

    def _save(self, value):
        self.db.save(self.url, value)
