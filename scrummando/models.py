from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from sqlalchemy.orm import relationship
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

def create_alternatives(question,question_data):
    alt1 = Alternatives(question_data[1])
    alt2 = Alternatives(question_data[2])
    alt3 = Alternatives(question_data[3])
    alt4 = Alternatives(question_data[4])
    DBSession.add(alt1)
    DBSession.add(alt2)
    DBSession.add(alt3)
    DBSession.add(alt4)

    question.alternatives.append(alt1)
    question.alternatives.append(alt2)
    question.alternatives.append(alt3)
    question.alternatives.append(alt4)

    DBSession.flush()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text)
    password = Column(Text)
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Alternatives(Base):
    __tablename__ = 'alternatives'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('questions.id'))
    text = Column(Text)
    def __init__(self,alternative):
        self.text = alternative

class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    correct_alternative_pos = Column(Integer)
    alternatives = relationship(Alternatives)
    def __init__(self,question_data):
        self.text = question_data[0]
        create_alternatives(self,question_data)
        self.correct_alternative_pos = int(question_data[5])

    




    
        

    
