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

    $ ./fetch_lpi.py
    http://www.lumosity.com/app/v4/training_history/summaries/2015-07-01
    Flexibility
            * Ebb and Flow: Android Phone:1703
            * Disillusion Mobile:1655
            * Disillusion (new):1648
            * Color Match:1645
            * Disillusion:1623
            * Word Bubbles Rising:1542
            * Brain Shift: Android Phone:1407
    Memory
            * Memory Matrix: Android Phone:1916
            * Memory Matrix:1878
            * Pinball Recall:1552
            * Pinball Recall Mobile:1505
            * Memory Match Overdrive:0
            * Memory Match (new):0
    Speed
            * Penguin Pursuit:1714
            * Speed Match:1564
            * Spatial Speed Match:1545
            * Speed Match Overdrive:1514
            * Speed Match: Android Phone:1506
            * Speed Pack:1415
            * Speed Pack Mobile:0
    Problem Solving
            * Chalkboard Challenge: Android Phone:1837
            * Pet Detective Mobile:1681
            * Raindrops:1603
            * Pet Detective:1524
            * Raindrops (new):0
            * Raindrops Mobile:0
    Attention
            * Train of Thought Mobile:1852
            * Observation Tower:1695
            * Lost in Migration: Android Phone:1598
            * Playing Koi:1581
            * Lost in Migration:1573
            * Trouble Brewing Mobile:1521
            * Star Search:1386
            * Rhythm Revolution:0
