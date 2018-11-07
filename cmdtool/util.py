#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Clean:

    def __init__(self, max_shops, body):
        self.max_shops = max_shops
        self.body = body

    def shopname(self):
        """
        :return: list of shops in string
        """
        name = ['店舗名']
        for i in range(0, self.max_shops):
            name.append(self.body[i]['name'])
        return name

    def address(self):
        """
        :return: list of shop address in string
        """
        address = ['住所']
        for i in range(0, self.max_shops):
            clean_address = self.body[i]['address'].replace('\u3000', '')
            address.append(clean_address)
        return address

    def lat(self):
        """
        :return: list of shop latitude in float
        """
        lat = ['緯度']
        for i in range(0, self.max_shops):
            number_lat = float(self.body[i]['lat'])
            lat.append(number_lat)
        return lat

    def lng(self):
        """
        :return: list of shop longitude in float
        """
        lng = ['経度']
        for i in range(0, self.max_shops):
            number_lng = float(self.body[i]['lng'])
            lng.append(number_lng)
        return lng

    def capacity(self):
        """
        :return: list of shop capacity in integer
        """
        capacity = ['収容人数']
        for i in range(0, self.max_shops):
            int_capacity = int(self.body[i]['capacity'])
            capacity.append(int_capacity)
        return capacity

    def genre(self):
        """
        :return: list of shop genre in string
        """
        genre = ['ジャンル']
        for i in range(0, self.max_shops):
            str_genre = str(self.body[i]['genre']['name'])
            genre.append(str_genre)
        return genre

    def midnight(self):
        """
        :return: list of shop midnight operation flag in string
        """
        midnight = ['深夜営業']
        for i in range(0, self.max_shops):
            str_midnight = str(self.body[i]['midnight'])
            midnight.append(str_midnight)
        return midnight


def save_csv(data_frame, file_name):
    """
    it will save the data as csv.
    :param data_frame: pandas data frame that has the data you want to save
    :param file_name: file_name: csv file name you want to save
    :return:
    """
    current_dir = os.getcwd()
    path = current_dir + '/' + str(file_name)
    data_frame.to_csv(path, encoding="utf-8")
    pass


