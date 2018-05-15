#! python3
#trying to display headlines with python3.
import requests, sys, bs4, os, time
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))
feed=requests.get('https://www.wired.com/feed/rss')
feed.raise_for_status()
wired=bs4.BeautifulSoup(feed.text,"html.parser")
titleE=wired.select('title')
for i in titleE:
    print(i.getText())
    text=i.getText()
    notify(title="Dose of news",subtitle=text,message="Have fun")
    time.sleep(3)
