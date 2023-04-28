import pathlib

import pandas

from api.database import *

path = pathlib.Path(
    r'C:\Users\SakuraPuare\Desktop\计算机设计大赛\中国的碳减排与世界能源消费\data\1997-2017年中国县级尺度碳排放.CSV')

if __name__ == '__main__':
    # create database
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    db.create_all_table()

    # open xlsx file
    with open(path, 'r') as f:
        data = pandas.read_csv(f, header=0)
    for row in data.itertuples():
        dist_code, county, county_en, city, city_en, province, province_en = row[1:8]
        insert = []
        for t, x in enumerate(row[8:]):
            year = 1997 + t
            carbon_emission = x
            emission = province_emission(year=year, province=province, city=city, county=county,
                                         province_en=province_en, city_en=city_en, county_en=county_en,
                                         carbon_emission=carbon_emission, dist_code=dist_code)
            insert.append(emission)
            pass
        db.inserts(insert)
