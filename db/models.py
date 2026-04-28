from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(100))
    first_name = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    subscriptions = relationship("Subscription", back_populates="user")


class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    case_number = Column(String(50), unique=True, nullable=False)
    plaintiff = Column(Text)
    defendant = Column(Text)
    judge = Column(String(200))
    status = Column(String(50), default='В производстве')
    url_kad = Column(Text)
    raw_data = Column(JSON)
    last_parsed_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    events = relationship("CaseEvent", back_populates="case")
    subscriptions = relationship("Subscription", back_populates="case")


class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    case_id = Column(Integer, ForeignKey('cases.id'), nullable=False)

    notify_one_side = Column(Boolean, default=True)
    notify_all = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)
    subscribed_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="subscriptions")
    case = relationship("Case", back_populates="subscriptions")


class CaseEvent(Base):
    __tablename__ = 'case_events'
    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey('cases.id'), nullable=False)
    event_type = Column(String(50), nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text)
    is_one_side = Column(Boolean, default=False)
    published_at = Column(DateTime)
    raw_source = Column(JSON)

    case = relationship("Case", back_populates="events")
