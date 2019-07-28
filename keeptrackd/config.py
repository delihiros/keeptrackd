import json

SETTINGS_FILENAME = 'settings.json'

def add(key, value):
    values = None
    with open(SETTINGS_FILENAME, 'r') as f:
        values = json.load(f)
        values[key] = value
    with open(SETTINGS_FILENAME, 'w') as f:
        json.dump(values, f, ensure_ascii=False, indent=2, sort_keys=True, separators=(',', ': '))

def get(key):
    with open(SETTINGS_FILENAME, 'r') as f:
        values = json.load(f)
        return values.get(key)