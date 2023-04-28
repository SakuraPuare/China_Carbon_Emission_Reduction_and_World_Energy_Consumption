import pathlib

import pandas

from api.database import *

path = pathlib.Path(
    r'C:\Users\SakuraPuare\Desktop\计算机设计大赛\中国的碳减排与世界能源消费\data\CarbonMonitor.csv')

if __name__ == '__main__':
    # create database
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    db.create_all_table()

    # open xlsx file
    with open(path, 'r', encoding='u8') as f:
        data = pandas.read_csv(f, header=0)
    for row in data.itertuples():
        insert = []
        country, carbon_emission, types, date = row[1:]
        year, month, day = date.split('-')
        insert.append(carbon_monitor(country=country, year=year, month=month, day=day, carbon_emission=carbon_emission,
                                     types=types))
        db.inserts(insert)
        pass
