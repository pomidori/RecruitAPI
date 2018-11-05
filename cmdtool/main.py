#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
from cmdtool.call_api import CallAPI
from cmdtool import util


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-max",  type=int, default=200,
                        help="maximum number of shop records to call.")
    parser.add_argument("-la", type=str, default='Z011',
                        help="Recruit API parameter to specify large area")
    parser.add_argument("-sf", type=str, default="csv",
                        help="save data in csv")
    args = parser.parse_args()
    sys.stdout.write(str(augment(args)))


def augment(args):
    if args.sf == "csv":
        max_shops = args.max
        large_area = args.la

        call = CallAPI(max_shops=max_shops, large_area=large_area)
        body = call.shops()
        data = call.format(body)

        # save data frame as a csv file
        util.save_csv(data_frame=data, file_name="data_0.csv")
        print("data_0.csv was successfully saved at the working directory")
        pass


if __name__ == '__main__':
    main()