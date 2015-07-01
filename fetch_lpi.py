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


def main(date):
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
    return stats


def print_stats(stats):
    for area in stats.keys():
        print(area)
        for game, lpi in sorted(stats[area].items(), key=operator.itemgetter(1),
                reverse=True):
            print('\t* {}:{}'.format(game, lpi))



def parse_args():
    parser = argparse.ArgumentParser(description='List your Games LPIs')
    parser.add_argument('-d', action="store", dest='date',
                        help='date (yyyy-mm-dd) [default today]')
    parser.add_argument('-s', action="store", dest='span', default=8,
                        help='number of history days to crawl [default 8]')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    stats = {}
    if not args.date:
        for i in range(args.span):
            date = datetime.datetime.today() - datetime.timedelta(i)
            day_stats = main(date.strftime("%Y-%m-%d"))
            for area in day_stats.keys():
                if not area in stats.keys():
                    stats[area] = {}
                for game in day_stats[area].keys():
                    if not game in stats[area].keys():
                        stats[area][game] = day_stats[area][game]
    else:
        stats = main(args.date)

    print_stats(stats)
