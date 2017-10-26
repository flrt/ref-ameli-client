#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Client de consultation des flux ATOM du référentiel AMELI

"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import argparse

import ameli


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", help="URL du flux ATOM")
    parser.add_argument("--date", help="Date à comparer. Format YYYY-MM-DD")
    parser.add_argument("--version", help="Version à comparer")
    args = parser.parse_args()

    check = ameli.Checker(args.url)
    print("Last updated (feed) : {}".format(check.get_updated_feed()))

    if args.version:
        check.infos_entries_post_version(args.version)

    if args.date:
        check.infos_entries_post_date(args.date)


if __name__ == "__main__":
    main()
