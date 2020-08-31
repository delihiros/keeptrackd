from keeptrackd import (
        tracker
        )

ComicRyuTracker = tracker.common.build_simple_tracker(
        'ComicRyuTracker',
        r'https://comic-ryu.jp/[^/]+/index.html',
        '#read > ul > li:nth-child(1) > p.readbtn > a > span',
        lambda self: print(self.url))
