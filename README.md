# lumosity_tools
Tools to get more efficient when training at Lumosity


# Installation

Build your virtual environment with python 3:

    $ mkvirtualenv -p /usr/bin/python3.4 lumosity

Install the dependencies:

    $ pip install -r requirements.txt

Create a new file `local_settings.py` and add your email/password credentials
there:

    # local_settings.py 
    EMAIL = "you@example.com"
    PASSWORD = "your_lumosity_password"


# Usage

Get ordered list of games LPI. This allows you to quickly find what game you
need to train in order to improve your overall LPI (note: LPI=0 is for games
without LPI, if you didn't play them 5 times)

    $ ./fetch_lpi.py --help                                                                          ✱
    usage: fetch_lpi.py [-h] [-d DATE] [-s SPAN]

    List your Games LPIs

    optional arguments:
      -h, --help  show this help message and exit
      -d DATE     date (yyyy-mm-dd) [default today]
      -s SPAN     number of history days to crawl [default 8]

    $ ./fetch_lpi.py
    http://www.lumosity.com/app/v4/training_history/summaries/2015-07-01
    http://www.lumosity.com/app/v4/training_history/summaries/2015-06-30
    http://www.lumosity.com/app/v4/training_history/summaries/2015-06-29
    http://www.lumosity.com/app/v4/training_history/summaries/2015-06-28
    http://www.lumosity.com/app/v4/training_history/summaries/2015-06-27
    http://www.lumosity.com/app/v4/training_history/summaries/2015-06-26
    http://www.lumosity.com/app/v4/training_history/summaries/2015-06-25
    http://www.lumosity.com/app/v4/training_history/summaries/2015-06-24
    Memory
            * Memory Matrix: Android Phone:1916
            * Memory Matrix:1878
            * Rotation Matrix:1670
            * Pinball Recall:1552
            * Tidal Treasures Mobile:1517
            * Pinball Recall Mobile:1505
            * Moneycomb:1352
            * Memory Match Mobile:1297
            * Memory Match:1156
            * Follow That Frog:1139
            * Memory Match Overload:1025
            * Familiar Faces:739
            * Memory Lane:365
            * Rhyme Workout:358
            * Memory Match Overdrive:0
            * Memory Match (new):0
    Attention
            * Train of Thought Mobile:1852
            ...


# What next ?

## fetch_lpi.py

* Save results in sqlite database
* Add cron/timer to auto-parse new results daily
* Only return best/worst games (and return fast) when querying script

## Other scripts

I have no plan to add more scripts at the moment, but if you have any idea,
feel free to request it in a ticket.
