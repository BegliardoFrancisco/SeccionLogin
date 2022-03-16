from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import  declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://postgres:250210@localhost:3306/UserManager'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL,
					echo =True,)

SeccionLocal = sessionmaker(engine,
						expire_on_commit=False,
						class_=AsyncSession)

Base =	declarative_base()

