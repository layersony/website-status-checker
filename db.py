from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class Website(Base):
    __tablename__ = 'websites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False)

def init_db():
    DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URI')
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    websites = [
        Website(url="http://example.com"),
        Website(url="http://example2.com")
    ]
    
    session.add_all(websites)
    session.commit()
    session.close()

if __name__ == '__main__':
    init_db()
