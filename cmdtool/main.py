#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
from call_api import CallAPI
from util import save_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-key", type=str, default=None,
                        help="provide your developer key for the API")
    parser.add_argument("-max",  type=int, default=200,
                        help="maximum number of shop records to call.")
    parser.add_argument("-la", type=str, default='Z011',
                        help="Recruit API parameter to specify large area")
    parser.add_argument("-sf", type=str, default="csv",
                        help="save data in csv")
    args = parser.parse_args()
    sys.stdout.write(str(augment(args)))


def augment(args):
    if args.key is None:
        create_account_url = "https://webservice.recruit.co.jp/register/index.html"
        raise ValueError(
            '''
            developer key is not provided. 
            Please register and create your own key here:{}
            '''.format(create_account_url))
    elif args.sf == "csv":
        key = args.key
        max_shops = args.max
        large_area = args.la

        call = CallAPI(key=key, max_shops=max_shops, large_area=large_area)
        body = call.shops()
        data = call.format(body)

        # save data frame as a csv file
        save_csv(data_frame=data, file_name="data_0.csv")
        print("data_0.csv was successfully saved at the working directory")
        pass


if __name__ == '__main__':
    main()