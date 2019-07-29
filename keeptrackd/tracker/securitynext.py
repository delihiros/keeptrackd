from keeptrackd import (
        tracker
        )

SecurityNextTracker = tracker.common.build_simple_tracker(
        'SecurityNextTracker',
        r'https?://www.security-next.com/',
        '#wrapper > div.main > div.content > div:nth-child(7) > a',
        lambda self: print(self.url))
