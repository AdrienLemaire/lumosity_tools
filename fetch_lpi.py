#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import datetime
import json
import os.path
import requests

from local_settings import EMAIL, PASSWORD


def main(date=datetime.datetime.today().strftime("%Y-%M-%d")):
    with requests.Session() as s:
        # 1. login
        url = 'https://www.lumosity.com/login'
        s.get(url, verify=True)  # get cookies
        payload = {
            'email': EMAIL,
            'password': PASSWORD,
            #'csrfmiddlewaretoken': s.cookies['csrftoken'],
        }
        s.post(url, data=payload, headers={'Referer': url})
        import ipdb; ipdb.set_trace()

        # 2. Get 
        url = 'http://www.lumosity.com/app/v4/training_history/summaries/{}'
        r = s.get(url.format(date))
        print r.url


def parse_args():
    parser = argparse.ArgumentParser(description='List your Games LPIs')
    parser.add_argument('-i', action="store", dest='item',
                        help='date (yyyy-mm-dd)')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args.item)
