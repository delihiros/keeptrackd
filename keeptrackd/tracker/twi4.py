import re
from urllib.parse import urljoin

from keeptrackd import (
        browser,
        dbmanager,
        tracker
        )


class Twi4Tracker(tracker.common.Tracker):

    valid_url_re = re.compile(r'https?://sai-zen-sen.jp/comics/twi4/.+$')

    def __init__(self, url):
        self.url = url
        self.browser = browser.Browser()
        self.db = dbmanager.DBManager()

    @classmethod
    def suitable(cls, url):
        return cls.valid_url_re.match(url) is not None

    def check_update(self):
        latest_work_number = self._get_latest()
        last_time = self._get_last_time()
        if not last_time or latest_work_number != last_time:
            self._save(latest_work_number)
            return True
        return None

    def postprocess(self):
        latest_url = urljoin(self.url, self.latest_work_number.zfill(4) + '.html')
        print(latest_url)

    def _get_latest(self):
        self.browser.get(self.url)
        self.page_source = self.browser.page_source
        self.latest_work_number = self.browser.find_element_by_css_selector('#comics > div > article:last-child > header > div > h3 > span.work-number').text
        return self.latest_work_number

    def _get_last_time(self):
        result = self.db.get(self.url)
        if result:
            return result[1]
        return None

    def _save(self, value):
        self.db.save(self.url, value)
