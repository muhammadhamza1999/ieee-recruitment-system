from sqlalchemy import Column,Boolean,LargeBinary,ForeignKey,Binary,CHAR,String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Registration(base):
    __tablename__ = 'registration'

    id = Column(CHAR(5),primary_key=True)
    name = Column(String(32),nullable=False)
    email = Column(String(50),nullable=False,unique=True)
    phone_number = Column(CHAR(11),nullable=False)
    cnic = Column(CHAR(13),nullable=False,unique=True)
    year = Column(String(6),nullable=False)
    domain = Column(String(25),nullable=False)
    discipline = Column(String(30),nullable=False)
    about = Column(String,nullable=False)
    association = Column(String,nullable=False)
    why = Column(String,nullable=False)
    achievements = Column(String,nullable=True)
    status = Column(Boolean,default=False)
    reviewed = Column(Boolean,default=False)
    selection_status = Column(CHAR(1),default='3')
    imagestore = relationship("Imagestore", uselist=False, back_populates="registration")
    interview = relationship("Interview", uselist=False, back_populates="registration")


    def __init__(self,id,name,email,phone_number,cnic,year,domain,discipline,about,association,why,achievements):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.cnic = cnic
        self.year = year
        self.domain = domain
        self.discipline = discipline
        self.about = about
        self.association = association
        self.why = why
        self.achievements = achievements


class Imagestore(base):
    __tablename__ = 'imagestore'

    reg_id = Column(CHAR(5), ForeignKey('registration.id'),primary_key=True)
    data = Column(LargeBinary, nullable=False)
    registration = relationship("Registration", back_populates="imagestore")

    def __init__(self, data):
        self.data = data

class Admin(base):
    __tablename__='admin'

    email = Column(String(50),primary_key=True)
    password = Column(Binary(60),nullable=False)

    def __init__(self,email,password):
        self.email=email
        self.password=password

class Interview(base):
    __tablename__='interview'

    reg_id = Column(CHAR(5), ForeignKey('registration.id'),primary_key=True)
    scores = Column(ARRAY(CHAR(1), dimensions=1),nullable=True)
    remarks = Column(String,nullable=True)
    show_feedback = Column(Boolean,default=False)
    registration = relationship("Registration", back_populates="interview")

