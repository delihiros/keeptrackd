import re
import hashlib
import time

from keeptrackd import (
        browser,
        dbmanager
        )


class Tracker:

    valid_url_re = re.compile(r'.+$')

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
        self.page_source = self.browser.page_source()
        hs = hashlib.sha256(self.page_source.encode()).hexdigest()
        return hs

    def _get_last_time(self):
        result = self.db.get(self.url)
        if result:
            return result[1]
        return None

    def _save(self, value):
        self.db.save(self.url, value)


def build_simple_tracker(class_name, valid_url, css_selector, postprocessor_fn, wait_for=False):
    tracker_class = type(class_name, Tracker.__bases__, dict(Tracker.__dict__))
    tracker_class.valid_url_re = re.compile(valid_url)
    tracker_class.postprocess = postprocessor_fn

    def _get_latest(self):
        self.browser.get(self.url)
        if wait_for:
            elem = self.browser.wait_for(css_selector)
            return elem.text
        else:
            self.page_source = self.browser.page_source
            self.latest = self.browser.find_element_by_css_selector(css_selector).text
            return self.latest

    tracker_class._get_latest = _get_latest
    return tracker_class