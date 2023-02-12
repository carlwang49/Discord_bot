from sqlalchemy import Column, VARCHAR, BOOLEAN, ForeignKey, TIMESTAMP, Integer, BIGINT
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

# 使用者欄位
class User_info(BASE):
    __tablename__ = 'user_info'
    name = Column(VARCHAR, nullable = False)
    user_id = Column(BIGINT, nullable = False, primary_key = True, unique = True)
    points = Column(Integer, nullable = False)
    email = Column(VARCHAR, nullable = True)
    title = Column(VARCHAR , nullable = True)
    department = Column(VARCHAR, nullable = True)


class Emoji_info(BASE):
    __tablename__ = 'emoji_info'
    emoji_eng = Column(VARCHAR, nullable = False, primary_key = True, unique = True)
    emoji_id = Column(VARCHAR, nullable = False)
    emoji_name = Column(VARCHAR, nullable = True)


class Event_points(BASE):
    __tablename__ = 'event_points'
    name = Column(VARCHAR, nullable = False)
    user_id = Column(BIGINT, ForeignKey("user_info.user_id"), nullable = False, primary_key = True, unique = True)
    team_buying = Column(Integer, nullable = False, default = 0)
    working_report = Column(Integer, nullable = False, default = 0)
    docs_apply = Column(Integer, nullable = False, default = 300)

class Menu(BASE):
    __tablename__ = 'menu'
    number = Column(Integer, nullable=False, primary_key=True, unique=True)
    brand = Column(VARCHAR, nullable=False)
    item = Column(VARCHAR, nullable=False)
    price_small = Column(Integer, nullable=False)
    price_large = Column(Integer, nullable=False)

class Time_Sheet(BASE):

    __tablename__ = 'time_sheet'

    user_id = Column(VARCHAR, nullable=False, primary_key=True)
    user = Column(VARCHAR, nullable=False)
    department = Column(VARCHAR, nullable=False)
    datetime = Column(VARCHAR, nullable=False)
    project = Column(VARCHAR, nullable=False, primary_key=True)
    hours = Column(VARCHAR, nullable=False)


class Overtime_Sheet(BASE):

    __tablename__ = 'overtime_sheet'

    user_id = Column(VARCHAR, nullable=False, primary_key=True)
    user = Column(VARCHAR, nullable=False)
    project = Column(VARCHAR, nullable=False, primary_key=True)
    date = Column(VARCHAR, nullable=False)
    department = Column(VARCHAR, nullable=False)
    hours = Column(VARCHAR, nullable=False)
    status = Column(BOOLEAN)


class Leave_Sheet(BASE):

    __tablename__ = 'leave_sheet'

    user_id = Column(VARCHAR, nullable=False, primary_key=True)
    user = Column(VARCHAR, nullable=False)
    reason = Column(VARCHAR, nullable=False)
    department = Column(VARCHAR, nullable=False)
    apply_date = Column(VARCHAR, nullable=False)
    leave_date = Column(VARCHAR, nullable=False, primary_key=True)
    hours = Column(VARCHAR, nullable=False)
    status = Column(BOOLEAN)


class Profile(BASE):

    __tablename__ = 'user_profile'

    user_id = Column(VARCHAR, nullable=False, primary_key=True)
    user = Column(VARCHAR, nullable=False)
    title = Column(VARCHAR, nullable=False)
    department = Column(VARCHAR, nullable=False)

class MALL(BASE):

     __tablename__ = 'mall'

     commodity = Column(VARCHAR, nullable=False, primary_key=True)
     points = Column(VARCHAR, nullable=False)
     amount = Column(VARCHAR, nullable=False)
     image_url = Column(VARCHAR, nullable=False)
     description = Column(VARCHAR, nullable=False)