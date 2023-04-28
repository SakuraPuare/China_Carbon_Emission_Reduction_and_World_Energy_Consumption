import pathlib

from sqlalchemy import Integer, Column
from sqlalchemy.orm import DeclarativeBase

path = pathlib.Path(r'C:\Users\SakuraPuare\Desktop\计算机设计大赛\中国的碳减排与世界能源消费\data\30个省份排放清单')


class Base(DeclarativeBase):
    pass


class province_emission(Base):
    __tablename__ = 'province_emission'
    id = Column(Integer, primary_key=True, autoincrement=True)
    province = Column(Integer)
    year = Column(Integer)



if __name__ == '__main__':
    pass
