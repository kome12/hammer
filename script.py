import webbrowser
from decouple import config

WEBSITES = config('WEBSITES')
split_websites = WEBSITES.split(',')

for url in split_websites:
    webbrowser.open(url.encode('utf-8').strip(), 1)
