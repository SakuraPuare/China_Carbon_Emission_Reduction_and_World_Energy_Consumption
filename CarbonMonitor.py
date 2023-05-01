import pathlib

import pandas

from database import *

path = pathlib.Path(
    r'C:\Users\SakuraPuare\Desktop\计算机设计大赛\中国的碳减排与世界能源消费\data\CarbonMonitor.csv')

if __name__ == '__main__':
    # create database
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    db.create_all_table()

    # open xlsx file
    with open(path, 'r', encoding='u8') as f:
        data = pandas.read_csv(f, header=0)

    date_dict = {
        2019: {},
        2020: {},
        2021: {},
        2022: {}
    }

    for row in data[data.country == 'China'][data.sector == 'Total'].itertuples():
        date = datetime.datetime.strptime(row.date, '%Y-%m-%d')
        if date.year in date_dict:
            date_dict[date.year][date.month] = date_dict[date.year].get(date.month, 0.0) + row.co2

    insert = []
    for year, month_dict in date_dict.items():
        for month, value in month_dict.items():
            insert.append(carbon_monitor(year=year, month=month, value=value))
    db.inserts(insert)
