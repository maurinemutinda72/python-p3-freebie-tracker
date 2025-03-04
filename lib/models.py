from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker

Base = declarative_base()

# Company Model
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)

    # Relationships
    freebies = relationship("Freebie", back_populates="company", overlaps="devs,freebies")
    devs = relationship("Dev", secondary="freebies", back_populates="companies", overlaps="devs,freebies")

# Dev Model
class Dev(Base):
    __tablename__ = "devs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationships
    freebies = relationship("Freebie", back_populates="dev", overlaps="companies,freebies")
    companies = relationship("Company", secondary="freebies", back_populates="devs", overlaps="companies,freebies")

# Freebie Model
class Freebie(Base):
    __tablename__ = "freebies"

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))
    dev_id = Column(Integer, ForeignKey("devs.id"))

    # Relationships 
    company = relationship("Company", back_populates="freebies", overlaps="devs,freebies")
    dev = relationship("Dev", back_populates="freebies", overlaps="companies,freebies")

# Database Setup
engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()
