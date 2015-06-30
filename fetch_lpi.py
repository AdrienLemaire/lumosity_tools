#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from bs4 import BeautifulSoup as bs
import datetime
import json
import operator
import os.path
import requests

from local_settings import EMAIL, PASSWORD


def main(date=None):
    if not date:
        date = datetime.datetime.today().strftime("%Y-%m-%d")
    data = {}
    with requests.Session() as s:
        # 1. login
        url = 'https://www.lumosity.com/login'
        s.get(url, verify=True)  # get cookies
        payload = {
            'user[login]': EMAIL,
            'user[password]': PASSWORD,
            #'csrfmiddlewaretoken': s.cookies['csrftoken'],
        }
        s.post(url, data=payload, headers={'Referer': url})

        # 2. Get 
        url = 'http://www.lumosity.com/app/v4/training_history/summaries/{}'
        print(url.format(date))
        r = s.get(url.format(date))
        content = r.content
        p = bs(r.content)
        raw= str([s for s in p.find_all('script') if "Summaries.Show.init" in
            s.text][0])
        data = json.loads(raw[raw.find('{', raw.find('{')+1):raw.rfind('}', 0,
            raw.rfind('}'))+1])

    results = data['calendarData'][0]['data']['results']
    stats = {}

    for day_result in data['calendarData']:
        results = day_result['data']['results']
        for area in results.keys():
            if not area in stats.keys():
                stats[area] = {}
            for game in results[area]:
                if not game['game'] in stats[area].keys():
                    stats[area][game['game']] = game['bpi'] or 0

    for area in stats.keys():
        print(area)
        for game, lpi in sorted(stats[area].items(), key=operator.itemgetter(1),
                reverse=True):
            print('\t* {}:{}'.format(game, lpi))



def parse_args():
    parser = argparse.ArgumentParser(description='List your Games LPIs')
    parser.add_argument('-i', action="store", dest='item',
                        help='date (yyyy-mm-dd)')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args.item)
