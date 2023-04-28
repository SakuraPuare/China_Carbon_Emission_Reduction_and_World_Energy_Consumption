from typing import Union, Iterable

from sqlalchemy import create_engine, String, Column, Float, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(db_url, echo=True)
        self.session = sessionmaker(bind=self.engine)()

    def init(self) -> None:
        self.create_all_table()

    def create_all_table(self) -> None:
        Base.metadata.create_all(self.engine)

    def inserts(self, obj: Union[Iterable[Base], Base]) -> None:
        if isinstance(obj, list):
            self.session.add_all(obj)
        else:
            self.session.add(obj)
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.close()

    def close(self) -> None:
        self.session.close()
        self.engine.dispose()


class province_emission(Base):
    __tablename__ = 'province_emission'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer)
    province = Column(String(255))
    city = Column(String(255))
    county = Column(String(255))
    province_en = Column(String(511))
    city_en = Column(String(511))
    county_en = Column(String(511))
    carbon_emission = Column(Float)
    dist_code = Column(String(255))

    def __repr__(self):
        return f'<province_emission(year={self.year}, province={self.province}, city={self.city}, county={self.county}, province_en={self.province_en}, city_en={self.city_en}, county_en={self.county_en}, carbon_emission={self.carbon_emission}, dist_code={self.dist_code})>'


class global_county_emission(Base):
    __tablename__ = 'global_county_emission'
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(255))
    # country_en = Column(String(511))
    county_code = Column(String(127))
    types = Column(String(255))
    year = Column(Integer)
    emission = Column(Float)

    def __repr__(self):
        return f'<global_county_emission(country={self.country}, county_code={self.county_code}, types={self.types}, year={self.year}, emission={self.emission})>'


class province_emission_detail(Base):
    __tablename__ = 'province_emission_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    province = Column(String(255))
    year = Column(Integer)
    types = Column(String(255))
    carbon_emission = Column(Float)

    def __repr__(self):
        return f'<province_emission(province={self.province}, types={self.types}, carbon_emission={self.carbon_emission})>'


class province_detail(Base):
    __tablename__ = 'province_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    province = Column(String(255))
    year = Column(Integer)
    types = Column(String(255))
    carbon_emission = Column(Float)

    def __repr__(self):
        return f'<province_emission(province={self.province}, year={self.year}, carbon_emission={self.carbon_emission})>'


class city_detail(Base):
    __tablename__ = 'city_detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    province = Column(String(255))
    city = Column(String(255))
    year = Column(Integer)
    types = Column(String(255))
    carbon_emission = Column(Float)

    def __repr__(self):
        return f'<province_emission(city={self.city}, year={self.year}, carbon_emission={self.carbon_emission})>'


if __name__ == '__main__':
    db = Database('mysql+pymysql://root:20131114@localhost:3306/env?charset=utf8mb4')
    db.create_all_table()
