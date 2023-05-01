import time

from fastapi import FastAPI
from sqlalchemy import func

from database import *

app = FastAPI()

db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')


@app.get("/")
async def root():
    """ 测试接口
    """
    return {"message": "Hello World", "code": 200, "time": time.time()}


@app.get("/wordcloud")
async def get_wordcloud():
    """ 获取词云数据
    """
    # random 30
    data = db.session.query(word_freq.name, word_freq.value).order_by(func.rand()).limit(30).all()
    data = [{"name": i[0], "value": i[1]} for i in data]
    return {"data": data}


@app.get("/china_carbon")
async def get_china_carbon():
    """ 获取中国碳排放数据
    """
    data = []
    for year in range(2019, 2023):
        t = db.session.query(carbon_monitor.value).filter(carbon_monitor.year == year).order_by(
            carbon_monitor.month).all()
        data.append({"label": str(year) + '年', "value": [i[0] for i in t]})
    return {"data": data}

#
# @app.get("/china_city_list")
# async def china_city_list():
#     """ 获取所有地级市列表
#
#     :return: 直接返回所有地级市列表
#     """
#     return china_country
#
#
# @app.get("/global_country_list")
# async def global_country_list():
#     """ 获取所有国家列表
#
#     :return: 直接返回所有国家列表及其代码
#     """
#     return global_country
#
#
# @app.get("/china_carbon/{province}")
# async def china_carbon_province(province: str, year: int = None):
#     """ 获取指定省份的碳排放数据
#
#     :param province: 省份名称
#     :param year: 年份, 默认为 None, 返回所有年份的数据
#     :return: data: 碳排放数据, year_list: 年份列表
#     """
#     # sort by year
#     if year is not None:
#         ans = db.session.query(province_detail).filter(province_detail.province == province,
#                                                        province_detail.year == year).order_by(
#             province_detail.year).all()
#     else:
#         ans = db.session.query(province_detail).filter(province_detail.province == province).order_by(
#             province_detail.year).all()
#     year_list = set([i.year for i in ans])
#     return {"data": ans, "year_list": year_list}
#
#
# @app.get("/china_carbon/{province}/{city}")
# async def china_carbon_city(province: str, city: str, year: int = None):
#     """ 获取指定地级市的碳排放数据
#
#     :param province: 省份名称
#     :param city: 地级市名称
#     :param year: 年份, 默认为 None, 返回所有年份的数据
#     :return: data: 碳排放数据, year_list: 年份列表
#     """
#     # sort by year
#     if year is not None:
#         ans = db.session.query(city_detail).filter(city_detail.province == province, city_detail.city == city,
#                                                    city_detail.year == year).order_by(
#             city_detail.year).all()
#     else:
#         ans = db.session.query(city_detail).filter(city_detail.province == province, city_detail.city == city).order_by(
#             city_detail.year).all()
#     year_list = set([i.year for i in ans])
#     return {"data": ans, "year_list": year_list}
#
#
# @app.get("/china_carbon/{province}/{city}/{county}")
# async def china_carbon_county(province: str, city: str, county: str, year: int = None):
#     """ 获取指定地级县的碳排放数据
#
#     :param province: 省份名称
#     :param city: 地级市名称
#     :param county: 地级县名称
#     :param year: 年份, 默认为 None, 返回所有年份的数据
#     :return: data: 碳排放数据, year_list: 年份列表
#     """
#     # sort by year
#     if year is not None:
#         ans = db.session.query(province_emission).filter(province_emission.province == province,
#                                                          province_emission.city == city,
#                                                          province_emission.county == county,
#                                                          province_emission.year == year).order_by(
#             province_emission.year).all()
#     else:
#         ans = db.session.query(province_emission).filter(
#             province_emission.province == province,
#             province_emission.city == city,
#             province_emission.county == county).order_by(
#             province_emission.year).all()
#     year_list = set([i.year for i in ans])
#     return {"data": ans, "year_list": year_list}
#
#
# @app.get("/global_carbon/{country}")
# async def global_carbon_country(country: str, year: int = None):
#     """ 获取指定国家的碳排放数据
#
#     :param country: 国家名称
#     :param year: 年份, 默认为 None, 返回所有年份的数据
#     :return: data: 碳排放数据, year_list: 年份列表
#     """
#     # sort by year
#     if year is not None:
#         ans = db.session.query(global_county_emission).filter(global_county_emission.country == country,
#                                                               global_county_emission.year == year,
#                                                               global_county_emission.types == "二氧化碳排放量（千吨）").order_by(
#             global_county_emission.year).all()
#     else:
#         ans = db.session.query(global_county_emission).filter(global_county_emission.country == country,
#                                                               global_county_emission.types == "二氧化碳排放量（千吨）").order_by(
#             global_county_emission.year).all()
#     year_list = set([i.year for i in ans])
#     return {"data": ans, "year_list": year_list}
