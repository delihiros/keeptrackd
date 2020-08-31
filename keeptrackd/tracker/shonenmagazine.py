from keeptrackd import (
        tracker
        )

ShonenMagazineTracker = tracker.common.build_simple_tracker(
        'ShonenMagazineTracker',
        r'https?://pocket.shonenmagazine.com/',
        '#page-viewer > section.series-information.type-episode > div.series-contents > div.js-readable-product-list > div.latest-readable-product-list.js-latest-readable-product-list > ul > li:nth-child(2) > a > div.series-episode-list-title-wrapper.test-readable-product-item-title > h4',
        lambda self: print(self.url),
        wait_for=True)
