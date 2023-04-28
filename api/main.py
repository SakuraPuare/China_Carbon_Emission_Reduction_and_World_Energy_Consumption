import json
import pathlib
import time

from fastapi import FastAPI

from database import *

app = FastAPI()

china_country_file = pathlib.Path('../china_country.json')
global_county_file = pathlib.Path('../global_country.json')
assert china_country_file.exists(), 'china_country not found'
assert global_county_file.exists(), 'global_country not found'

with open(china_country_file, 'r', encoding='u8') as f:
    china_country = json.load(f)

with open(global_county_file, 'r', encoding='u8') as f:
    global_country = json.load(f)

db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')


@app.get("/")
async def root():
    """ 测试接口
    """
    return {"message": "Hello World", "code": 200, "time": time.time()}


@app.get("/china_city_list")
async def china_city_list():
    """ 获取所有地级市列表

    :return: 直接返回所有地级市列表
    """
    return china_country


@app.get("/global_country_list")
async def global_country_list():
    """ 获取所有国家列表

    :return: 直接返回所有国家列表及其代码
    """
    return global_country


@app.get("/china_carbon/{province}")
async def china_carbon_province(province: str, year: int = None):
    """ 获取指定省份的碳排放数据

    :param province: 省份名称
    :param year: 年份, 默认为 None, 返回所有年份的数据
    :return: data: 碳排放数据, year_list: 年份列表
    """
    # sort by year
    if year is not None:
        ans = db.session.query(province_detail).filter(province_detail.province == province,
                                                       province_detail.year == year).order_by(
            province_detail.year).all()
    else:
        ans = db.session.query(province_detail).filter(province_detail.province == province).order_by(
            province_detail.year).all()
    year_list = set([i.year for i in ans])
    return {"data": ans, "year_list": year_list}


@app.get("/china_carbon/{province}/{city}")
async def china_carbon_city(province: str, city: str, year: int = None):
    """ 获取指定地级市的碳排放数据

    :param province: 省份名称
    :param city: 地级市名称
    :param year: 年份, 默认为 None, 返回所有年份的数据
    :return: data: 碳排放数据, year_list: 年份列表
    """
    # sort by year
    if year is not None:
        ans = db.session.query(city_detail).filter(city_detail.province == province, city_detail.city == city,
                                                   city_detail.year == year).order_by(
            city_detail.year).all()
    else:
        ans = db.session.query(city_detail).filter(city_detail.province == province, city_detail.city == city).order_by(
            city_detail.year).all()
    year_list = set([i.year for i in ans])
    return {"data": ans, "year_list": year_list}


@app.get("/china_carbon/{province}/{city}/{county}")
async def china_carbon_county(province: str, city: str, county: str, year: int = None):
    """ 获取指定地级县的碳排放数据

    :param province: 省份名称
    :param city: 地级市名称
    :param county: 地级县名称
    :param year: 年份, 默认为 None, 返回所有年份的数据
    :return: data: 碳排放数据, year_list: 年份列表
    """
    # sort by year
    if year is not None:
        ans = db.session.query(province_emission).filter(province_emission.province == province,
                                                         province_emission.city == city,
                                                         province_emission.county == county,
                                                         province_emission.year == year).order_by(
            province_emission.year).all()
    else:
        ans = db.session.query(province_emission).filter(
            province_emission.province == province,
            province_emission.city == city,
            province_emission.county == county).order_by(
            province_emission.year).all()
    year_list = set([i.year for i in ans])
    return {"data": ans, "year_list": year_list}


@app.get("/global_carbon/{country}")
async def global_carbon_country(country: str, year: int = None):
    """ 获取指定国家的碳排放数据

    :param country: 国家名称
    :param year: 年份, 默认为 None, 返回所有年份的数据
    :return: data: 碳排放数据, year_list: 年份列表
    """
    # sort by year
    if year is not None:
        ans = db.session.query(global_county_emission).filter(global_county_emission.country == country,
                                                              global_county_emission.year == year,
                                                              global_county_emission.types == "二氧化碳排放量（千吨）").order_by(
            global_county_emission.year).all()
    else:
        ans = db.session.query(global_county_emission).filter(global_county_emission.country == country,
                                                              global_county_emission.types == "二氧化碳排放量（千吨）").order_by(
            global_county_emission.year).all()
    year_list = set([i.year for i in ans])
    return {"data": ans, "year_list": year_list}
