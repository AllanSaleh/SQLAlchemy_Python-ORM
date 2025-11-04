from sqlalchemy import create_engine, String, Integer, DateTime, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import datetime, date

# ORM -> Object Relational Mapper

# Connecting to our SQLite database

engine = create_engine('sqlite:///my_db.db')


Base = declarative_base() #Base is the base class that all Model classes will inherit from
# Giving attributes to behave like a database table

# Create a User Model Class

class Users(Base):
  __tablename__ = 'users' #Table name (lower plural form of resource)

  id: Mapped[int] = mapped_column(primary_key=True) #Mapped defines the dataType, mapped_column defines the constraints of the column
  username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String(350), unique=True, nullable=False)
  password: Mapped[str] = mapped_column(String(120), nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
  is_active: Mapped[bool] = mapped_column(Boolean, default=True)




Base.metadata.create_all(engine) #Keep at the bottom of your page