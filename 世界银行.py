import math
import pathlib

import pandas

from database import *

path = pathlib.Path(
    r'C:\Users\SakuraPuare\Desktop\计算机设计大赛\中国的碳减排与世界能源消费\data\世界银行\二氧化碳强度（千克石油当量能源使用千克数）\API_EN.ATM.CO2E.EG.ZS_DS2_zh_csv_v2_5366911.csv')



if __name__ == '__main__':
    # create database
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    db.create_all_table()

    # open xlsx file
    with open(path, 'r', encoding='u8') as f:
        data = pandas.read_csv(f, header=4)
    for row in data.itertuples():
        country, country_code, types = row[1:4]
        if not isinstance(country, str):
            continue
        insert = []
        for t, x in enumerate(row[5:]):
            year = 1960 + t
            if math.isnan(x):
                continue
            emission = global_county_emission(country=country, county_code=country_code, types=types, year=year,
                                              emission=x)
            insert.append(emission)
        db.inserts(insert)
        pass
