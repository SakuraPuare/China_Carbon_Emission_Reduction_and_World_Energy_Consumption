import json

import numpy
from sqlalchemy import distinct

from api.database import *


def sum_province_emission() -> None:
    year_list = [i[0] for i in db.session.query(distinct(province_emission.year)).all()]
    province_list = [i[0] for i in db.session.query(distinct(province_emission.province)).all()]
    for year in year_list:
        insert = []
        for province in province_list:
            data = db.session.query(province_emission.carbon_emission).filter(province_emission.year == year,
                                                                              province_emission.province == province).all()
            s = numpy.sum(data)
            obj = province_detail(province=province, year=year, carbon_emission=s, types='carbon_emission')
            insert.append(obj)
        db.inserts(insert)


def sum_city_emission() -> None:
    year_list = [i[0] for i in db.session.query(distinct(province_emission.year)).all()]
    province_list = [i[0] for i in db.session.query(distinct(province_emission.province)).all()]
    for year in year_list:
        insert = []
        for province in province_list:
            city_list = [i[0] for i in db.session.query(distinct(province_emission.city)).filter(
                province_emission.province == province).all()]
            for city in city_list:
                data = db.session.query(province_emission.carbon_emission).filter(province_emission.year == year,
                                                                                  province_emission.province == province,
                                                                                  province_emission.city == city).all()
                s = numpy.sum(data)
                obj = city_detail(province=province, city=city, year=year, carbon_emission=s, types='carbon_emission')
                insert.append(obj)
        db.inserts(insert)


def get_all_county():
    county_dict = {}
    province_list = [i[0] for i in db.session.query(distinct(province_emission.province)).all()]
    for province in province_list:
        county_dict[province] = {}
        city_list = [i[0] for i in db.session.query(distinct(province_emission.city)).filter(
            province_emission.province == province).all()]
        for city in city_list:
            county_dict[province][city] = [i[0] for i in db.session.query(distinct(province_emission.county)).filter(
                province_emission.province == province, province_emission.city == city).all()]
    with open('china_country.json', 'w', encoding='u8') as f:
        json.dump(county_dict, f, ensure_ascii=False)


def get_all_country():
    country_dict = {i[0]: i[1] for i in db.session.query(distinct(global_county_emission.country),
                                                         global_county_emission.county_code).all()}
    with open('global_country.json', 'w', encoding='u8') as f:
        json.dump(country_dict, f, ensure_ascii=False)

def get_all_country_list():
    country_list = [i[0] for i in db.session.query(distinct(global_county_emission.country)).all()]
    country_list.extend()


def main() -> None:
    pass


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    # db.create_all_table()
    # sum_province_emission()
    # sum_city_emission()
    # get_all_county()
    # get_all_country()
    # print([i[0] for i in db.session.query(distinct(global_county_emission.types)).all()])