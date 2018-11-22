from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name,vote):
    cat_object = Cat(name=name,voter=vote)
    session.add(cat_object)
    session.commit()

def delete_cat_by_id(id):
	cat = session.query(Cat).filter_by(id=id).delete()
	session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def query_by_id(id):
   cat = session.query(
       Cat).filter_by(
       id=id).first()
   name = cat.name
   return name

def update_voter(id):
    cat = session.query(
       Cat).filter_by(
       id=id).first()
    cat.voter += 1
    session.commit()

