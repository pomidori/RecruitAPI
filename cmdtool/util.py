#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("..")


class Clean:

    def __init__(self, max_shops, body):
        self.max_shops = max_shops
        self.body = body

    def shopname(self):
        """
        :param body: number of shops
        :return: list of shops in string
        """
        name = ['店舗名']
        for i in range(0, self.max_shops):
            name.append(self.body[i]['name'])
        return name

    def address(self):
        """
        :param body: number of shops
        :return: list of shop address in string
        """
        address = ['住所']
        for i in range(0, self.max_shops):
            cleanaddress = self.body[i]['address'].replace('\u3000', '')
            address.append(cleanaddress)
        return address

    def lat(self):
        """
        :param body: number of shops
        :return: list of shop latitude in float
        """
        lat = ['緯度']
        for i in range(0, self.max_shops):
            numberlat = float(self.body[i]['lat'])
            lat.append(numberlat)
        return lat

    def lng(self):
        """
        :param body: number of shops
        :return: list of shop longitude in float
        """
        lng = ['経度']
        for i in range(0, self.max_shops):
            numberlng = float(self.body[i]['lng'])
            lng.append(numberlng)
        return lng

    def capacity(self):
        """

        :param body: number of shops
        :return: list of shop capacity in integer
        """
        capacity = ['収容人数']
        for i in range(0, self.max_shops):
            intcapacity = int(self.body[i]['capacity'])
            capacity.append(intcapacity)
        return capacity

    def genre(self):
        """
        :param body: number of shops
        :return: list of shop genre in string
        """
        genre = ['ジャンル']
        for i in range(0, self.max_shops):
            strgenre = str(self.body[i]['genre']['name'])
            genre.append(strgenre)
        return genre

    def midnight(self):
        """
        :param body: number of shops
        :return: list of shop midnight operation flag in string
        """
        midnight = ['深夜営業']
        for i in range(0, self.max_shops):
            strmidnight = str(self.body[i]['midnight'])
            midnight.append(strmidnight)
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


