import json
from keeptrackd import (
        dbmanager
        )

def get_chrome_bookmark_data(bookmark_path, dir_name):
    with open(bookmark_path) as f:
        bookmark_json = json.load(f)
        bookmark_bar = bookmark_json.get('roots').get('bookmark_bar')
        bookmark_dir = next(entry for entry in bookmark_bar.get('children') if entry.get('name') == dir_name)
        return [entry.get('url') for entry in bookmark_dir.get('children')]
