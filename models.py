import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, Integer, String

def today():
    return datetime.datetime.today().strftime("%Y-%m-%d")

class Osoba(Model):
    id = Column(Integer, primary_key=True)
    jmeno = Column(String(40), nullable=False)
    prijmeni = Column(String(40), nullable=False)
    datum = Column(Date)
    datum_vlozeni = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.jmeno