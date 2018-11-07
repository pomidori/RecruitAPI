#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
from util import Clean
import pandas as pd


class CallAPI:
    """
    
    """
    def __init__(self, key, large_area, max_shops, file="json", start=0, min_count=10):
        """
        :param key: your developer key
        :param large_area: Recruit API parameter to specify area
        :param file: Type of data format you want to return: json or xml
        :param file: file type, json or xml
        :param start: starting position of call
        :param min_count: minimum unit for a call
        """
        # Initialize the parameters.
        self.key = str(key)
        self.large_area = large_area
        self.max_shops = max_shops
        self.file = file
        self.start = start
        self.min_count = min_count
        self.count = self.max_shops // self.min_count

    def shops(self):
        """
        Call recruit open api to extract required shop data.
        :return: A list of json of a shop within a list.
        Example: [[<json file of a shop>], [<json file of a shop>], ...]
        """
        body = []
        start_time = time.time()
        for i in range(1, self.count + 1):
            # Setting up the url.
            url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/' + \
                  '?key={}'.format(self.key) + \
                  '&large_area={}&format={}&start={}'.format(self.large_area, self.file, self.start)

            # Request api and extract the wanted shop entities in the returned json.
            response = requests.get(url)
            json = response.json()
            json_shops = json['results']['shop'][0:self.min_count]
            body.extend(json_shops)
            self.start += i * self.min_count

            # Print out the called records and time elapsed for every 100 shops.
            if len(body) % 100 == 0:
                end_time = time.time()
                time_elapsed = end_time - start_time
                print('| Called records: {} | Time: {:.2f} seconds |'.format(len(body), time_elapsed))
            else:
                continue
        return body

    def format(self, body):
        """
        it will process json data to extract desired entries.
        :param body: a list with entries corresponding to shops in the defined json format
        :return: pandas dataframe with columns: shop name, address, lng, lat, capacity, genre, and midnight
        """
        df = []
        clean = Clean(self.max_shops, body)

        df.append(clean.shopname())
        df.append(clean.address())
        df.append(clean.lng())
        df.append(clean.lat())
        df.append(clean.capacity())
        df.append(clean.genre())
        df.append(clean.midnight())

        pandas_df = pd.DataFrame(df).T
        return pandas_df







