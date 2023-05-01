import pathlib

import numpy
import pandas

from database import *

path = pathlib.Path(
    r'C:\Users\SakuraPuare\Desktop\计算机设计大赛\中国的碳减排与世界能源消费\data\省级碳排放清单_1997-2019.xlsx')

pro = ["Beijing", "Tianjin", "Hebei", "Shanxi", "Inner mongolia", "Liaoning", "Jilin", "Heilongjiang", "Shanghai",
       "Jiangsu", "Zhejiang", "Anhui", "Fujian", "Jiangxi", "Shandong", "Henan", "Hubei", "Hunan", "Guangdong",
       "Guangxi", "Hainan", "Chongqing", "Sichuan", "Guizhou", "Yunnan", "Shaanxi", "Gansu", "Qinghai", "Ningxia",
       "Xinjiang", ]

if __name__ == '__main__':
    # create database
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    db.create_all_table()

    # open xlsx file
    # with open(path, 'r', encoding='u8') as f:
    y = [str(i) for i in range(2015, 2020)]
    data_all = pandas.read_excel(path, sheet_name=y, header=0)
    for year in y:
        data = data_all.get(year)
        year = int(year)
        insert = []
        for i in range(0, 4):
            name = data.values[i][1]
            v = data.values[i][2:32]
            for t, x in numpy.ndenumerate(v):
                insert.append(
                    province_emission_detail(province=pro[t[0]], year=year, types=name, carbon_emission=x))
            pass
        co2 = data.values[4]
        co2_name = co2[0]
        co2_data = co2[2:32]
        for t, x in numpy.ndenumerate(co2_data):
            insert.append(
                province_emission_detail(province=pro[t[0]], year=year, types=co2_name, carbon_emission=x))
        db.inserts(insert)
