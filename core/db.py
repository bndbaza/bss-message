from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BASE_URL = 'mysql+pymysql://root:35739517@192.168.0.51:3307/InOut2'

engine = create_engine(BASE_URL)
Session = sessionmaker(bind=engine)
