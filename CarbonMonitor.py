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

    pass

    data_dict = {}
    for country in data.country.unique():
        data_dict[country] = {}

    for row in data[data.sector == 'Total'].itertuples():
        date = datetime.datetime.strptime(row.date, '%Y-%m-%d')
        data_dict[row.country][date.year] = data_dict[row.country].get(date.year, 0.0) + row.co2

    insert = []
    for country, value in data_dict.items():
        for year, co2 in value.items():
            insert.append(global_carbon(country=country, year=year, value=co2))
    db.inserts(insert)
