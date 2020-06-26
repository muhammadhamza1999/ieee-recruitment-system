from bcrypt import hashpw,gensalt
from sqlalchemy import create_engine
from os import environ
from models import *
from sqlalchemy.orm import sessionmaker


db = create_engine(environ['DATABASE_URL'])
Session = sessionmaker(bind=db)
base.metadata.create_all(db)

admins = {'ali@gmail.com':'qwerty','waqas@gmail.com':'noyoubloody','sikander@gmail.com':'youfuckin'}
session = Session()
for admin in admins:
    hash = hashpw(admins[admin].encode('utf-8'),gensalt())
    session.add(Admin(admin,hash))

session.commit()
session.close()

db.dispose()

