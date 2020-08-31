from .common import (
        Tracker
        )

from .twi4 import (
        Twi4Tracker
        )

from .comicwalker import (
        ComicWalkerTracker
        )

from .webace import (
        WebAceTracker
        )

from .tonarinoyj import (
        TonarinoYJTracker
        )

from .comicryu import (
        ComicRyuTracker
        )

from .securitynext import (
        SecurityNextTracker
        )

from .shonenmagazine import (
        ShonenMagazineTracker
        )

trackers = [
        Twi4Tracker,
        ComicWalkerTracker,
        WebAceTracker,
        TonarinoYJTracker,
        ComicRyuTracker,
        SecurityNextTracker,
        ShonenMagazineTracker,
        Tracker
    ]

def get_tracker(url):
    for tracker in trackers:
        if tracker.suitable(url):
            return tracker(url)
