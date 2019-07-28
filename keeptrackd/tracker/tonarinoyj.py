import re
from urllib.parse import urljoin
import requests
import json
from html.parser import HTMLParser

from keeptrackd import (
    browser,
    dbmanager,
    tracker
    )


class TonarinoYJTracker(tracker.common.Tracker):

    valid_url_re = re.compile(r'https?://tonarinoyj.jp/episode/.+$')

    def __init__(self, url):
        super(TonarinoYJTracker, self).__init__(url)

    
    def _get_latest(self):
        self.browser.get(self.url)
        self.page_source = self.browser.page_source
        data_latest_list_endpoint = self.browser.find_element_by_css_selector('#page-viewer > section.series-information > div.series-contents > div.js-readable-product-list').get_attribute('data-latest-list-endpoint')
        response = requests.get(data_latest_list_endpoint)
        json_data = json.loads(response.text)
        html_data = json_data['html']

        class TonarinoYJParser(HTMLParser):

            def __init__(self):
                super(TonarinoYJParser, self).__init__()
                set()
                self.data = None

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == 'img' and attrs.get('class') and attrs.get('class') == 'series-episode-list-thumb':
                    self.data = attrs.get('alt')

        parser = TonarinoYJParser()
        parser.feed(html_data)
        parser.close()

        return parser.data