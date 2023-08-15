import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func

from database import *

app = FastAPI()

db = Database('')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """ 测试接口
    """
    return {"message": "Hello World", "code": 200, "time": time.time()}


@app.get("/wordcloud")
async def get_wordcloud():
    """ 获取词云数据
    """
    try:
        # random 30
        data = db.session.query(word_freq.name, word_freq.value).order_by(func.rand()).limit(125).all()
        data = [{"name": i[0], "value": i[1]} for i in data]
        return {"data": data}
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return {"error": str(e)}


@app.get("/china_carbon")
async def get_china_carbon():
    """ 获取中国碳排放数据
    """
    try:
        data = []
        for year in range(2019, 2023):
            t = db.session.query(carbon_monitor.value).filter(carbon_monitor.year == year).order_by(
                carbon_monitor.month).all()
            data.append({"label": str(year) + '年', "value": [str(i[0]) for i in t]})
        return {"data": data}
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return {"error": str(e)}


@app.get("/global_top")
async def get_global_top():
    """ 获取全球碳排放数据
    """
    key = {
        "China": "中国",
        "ROW": "其他",
        "US": "美国",
        "EU27 & UK": "欧盟",
        "India": "印度",
        "Russia": "俄罗斯",
        "Japan": "日本",
        "Germany": "德国",
        "Brazil": "巴西",
        "UK": "英国",
        "Italy": "意大利",
        "France": "法国",
        "Spain": "西班牙",
    }

    try:
        data = db.session.query(global_carbon.id, global_carbon.country, global_carbon.value).filter(
            global_carbon.year == 2022,
            global_carbon.country != "WORLD",
            global_carbon != "ROW").order_by(
            global_carbon.value.desc()).limit(10).all()
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return {"error": str(e)}
    cnt = 1
    data_list = []
    for i in data:
        d = {
            "id": i[0],
            "pm": cnt,
            "sf": key[i[1]],
            "pfl": i[2]
        }
        cnt += 1
        data_list.append(d)
    return {"data": data_list}
