from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String,
                        Float,
                        Date)
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

engine = create_engine('sqlite:///darbuotojai.db')
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = "Darbuotojas"
    id = Column(type_=Integer, primary_key=True)
    vardas = Column(name="Vardas", type_=String)
    pavarde = Column(name="Pavardė", type_=String)
    gimimo_data = Column(name="Gimimo data", type_=Date)
    atlyginimas = Column(name="Atlyginimas", type_=Float)
    dirba_nuo = Column(name="Dirba nuo", type_=Date,default=date.today)

    def __init__(self, vardas, pavarde, gimimo_data, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return f"{self.id}: {self.vardas} {self.pavarde} ({self.gimimo_data}) - {self.atlyginimas}, dirba nuo - {self.dirba_nuo}"

Base.metadata.create_all(engine)